import account.forms
import account.views

from .forms import SignupForm
from .models import StudyUserParticipant, StudyUserResearcher
from .settings import (STUDYUS_STUDYUSER_GEN_USER_ID as GEN_USER_ID,
                       STUDYUS_STUDYUSER_USER_ID_LEN as USER_ID_LEN)


class BaseSignupView(account.views.SignupView):
    form_class = SignupForm

    def generate_username(self, form):
        """Fill username field with a short random string."""
        return GEN_USER_ID(USER_ID_LEN)


class ParticipantSignupView(BaseSignupView):
    template_name = 'account/signup_participant.html'

    def after_signup(self, *args, **kwargs):
        participant = StudyUserParticipant(user=self.created_user)
        participant.save()
        super(ParticipantSignupView, self).after_signup(*args, **kwargs)


class ResearcherSignupView(BaseSignupView):
    template_name = 'account/signup_researcher.html'

    def after_signup(self, *args, **kwargs):
        researcher = StudyUserResearcher(user=self.created_user)
        researcher.save()
        super(ResearcherSignupView, self).after_signup(*args, **kwargs)
