from django.views.generic.edit import FormView

from .forms import ParticipantCreationForm


class ParticipantSignupView(FormView):
    template_name = ("studyuser/participant_signup.html")
    form_class = ParticipantCreationForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save()
        return super(ParticipantSignupView, self).form_valid(form)
