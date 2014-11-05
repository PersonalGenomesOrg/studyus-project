from django.conf.urls import patterns, url

from .views import ParticipantSignupView

urlpatterns = patterns(
    '',

    url(r'^participant-signup/', ParticipantSignupView.as_view()),

)
