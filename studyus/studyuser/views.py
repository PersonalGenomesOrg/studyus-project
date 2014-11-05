from django.contrib.auth import login as auth_login
from django.utils.http import is_safe_url
from django.views.generic.edit import FormView

from .forms import StudyParticipantCreationForm, StudyParticipantLoginForm
from .settings_default import (
    STUDYUS_STUDYUSER_SIGNUP_SUCC_URL as SIGNUP_SUCC_URL,
    STUDYUS_STUDYUSER_LOGIN_SUCC_URL as LOGIN_SUCC_URL,
    )


class ParticipantSignupView(FormView):
    template_name = ("studyuser/participant_signup.html")
    form_class = StudyParticipantCreationForm

    def post(self, request, *args, **kwargs):
        self.success_url = getattr(request.POST, 'next', SIGNUP_SUCC_URL)
        return super(ParticipantSignupView, self).post(
            request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super(ParticipantSignupView, self).form_valid(form)


class StudyUserLoginBase(FormView):
    """Abstract base view for logging in StudyUser-derived users.

    Additional definitions needed are:
    - self.form_class (expected to be a StudyUserLogin-derived form)
    - self.template_name
    """
    def post(self, request, *args, **kwargs):
        form = self.get_form(form_class=self.get_form_class())
        if form.is_valid():
            self.success_url = getattr(request.POST, 'next', LOGIN_SUCC_URL)
            if not is_safe_url(url=self.success_url, host=request.get_host()):
                self.success_url = LOGIN_SUCC_URL
            auth_login(request, form.get_user())
        return super(StudyUserLoginBase, self).post(
            request, *args, **kwargs)


class ParticipantLoginView(StudyUserLoginBase):
    template_name = ("studyuser/participant_login.html")
    form_class = StudyParticipantLoginForm
