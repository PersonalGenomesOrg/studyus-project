import account.forms
import account.views

from .forms import SignupForm
from .settings import (STUDYUS_STUDYUSER_GEN_USER_ID as GEN_USER_ID,
                       STUDYUS_STUDYUSER_USER_ID_LEN as USER_ID_LEN)


class SignupView(account.views.SignupView):

    form_class = SignupForm

    def generate_username(self, form):
        """Fill username field with a short random string."""
        return GEN_USER_ID(USER_ID_LEN)


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm
