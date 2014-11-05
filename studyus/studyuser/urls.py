from django.conf.urls import patterns, url

from .views import ParticipantSignupView, ParticipantLoginView

urlpatterns = patterns(
    '',

    url(r'^participant-signup/', ParticipantSignupView.as_view()),
    url(r'^participant-login/', ParticipantLoginView.as_view()),
)
