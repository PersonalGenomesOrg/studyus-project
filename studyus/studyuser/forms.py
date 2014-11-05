from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import StudyParticipant, StudyAdmin


class StudyUserCreationForm(forms.Form):
    """Base form for StudyUser-type account creation with email and password.

    Base class, not functional on its own -- model must be defined.

    Notes:
        self.model is expected to be derived from the StudyUser base model.
    """
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
        studyuser = self.model.create(email=self.cleaned_data["email"])
        studyuser.user.set_password(self.cleaned_data["password1"])
        studyuser.user.save()
        studyuser.save()
        return studyuser


class StudyParticipantCreationForm(StudyUserCreationForm):
    """Form for creating a StudyParticipant"""
    model = StudyParticipant


class StudyAdminCreationForm(StudyUserCreationForm):
    """Form for creating a StudyAdmin"""
    model = StudyAdmin


class StudyUserLoginForm(forms.Form):
    """Base form for StudyUser-type account login.

    Base class, not functional on its own -- model must be defined.

    Notes:
        self.model is expected to be derived from the StudyUser base model.
        clean() applies Django's authenticate() to a User object and stores
          the authenticated object in self.user_cached. This authenticated
          version is needed to later use Django's auth_login.
        get_user() returns self.user_cached.
    """
    email = forms.EmailField(label=_("Email address"),
                             widget=forms.EmailInput)
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': _("Please enter a correct email and password. "
                           "Note that the password field is case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def clean(self):
        """Check that email and password match."""
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                studyuser_matched = self.model.objects.get(
                    user__email__iexact=email)
                user_cached = authenticate(
                    username=studyuser_matched.user.username,
                    password=password)
            except User.DoesNotExist:
                user_cached = None

            if user_cached is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login'
                )
            else:
                self.user_cached = user_cached
                self.confirm_login_allowed(studyuser_matched)

        return self.cleaned_data

    def confirm_login_allowed(self, studyuser):
        """Controls whether the given StudyUser may log in.

        Default behavior is to check studyuser.user.is_active.
        """
        if not studyuser.user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cached


class StudyParticipantLoginForm(StudyUserLoginForm):
    model = StudyParticipant


class StudyAdminLoginForm(StudyUserLoginForm):
    model = StudyAdmin
