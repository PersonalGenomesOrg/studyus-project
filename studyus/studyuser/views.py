import hashlib

from django.conf import settings

import account.views

from .forms import SignupForm


class SignupView(account.views.SignupView):

    form_class = SignupForm

    def generate_username(self, form):
        """
        User's username field is replaced with a hash derived from the email.

        The hash uses the site's SECRET_KEY as salt to make this a safe
        user identifier for anonymously identifying a user. The hash is then
        truncated to 30 characters because this is Django's username limit.
        """
        salted = form.cleaned_data['email'] + settings.SECRET_KEY
        return hashlib.sha1(salted).hexdigest()[:30]
