from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import SignupView

# from .views import LogoutView, ParticipantLoginView, ParticipantSignupView

urlpatterns = patterns(
    '',
    url(r'^signup/$', SignupView.as_view(), name='account_signup'),

    # url(r'^participant-signup/', ParticipantSignupView.as_view(),
    #    name='participant-signup'),

    # url(r'^login/', ParticipantLoginView.as_view(),
    #    name='login'),
    # url(r'logout/', LogoutView.as_view(), name='logout'),
)
