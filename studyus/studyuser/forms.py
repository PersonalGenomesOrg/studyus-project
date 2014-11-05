from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from .models import StudyParticipant


class ParticipantCreationForm(forms.Form):
    """Creates a StudyParticipant from the given email and password."""

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'email_not_unique': _("This email address already has an account.")
    }
    email = forms.EmailField(label=_("Email address"),
                             widget=forms.EmailInput)
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as " +
                                            "above, for verification."))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError(
                self.error_messages['email_not_unique'],
                code='email_not_unique'
            )
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self):
        participant = StudyParticipant(email=self.cleaned_data["email"])
        participant.user.set_password(self.cleaned_data["password1"])
        participant.user.save()
        return participant
