from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

import studyus.studyuser.views

urlpatterns = patterns(
    '',

    # Override the default django-user-accounts to prevent accidental usage.
    url(r"^account/signup/$", RedirectView.as_view(url='/'),
        name="account_signup"),
    url(r"^account/signup/researcher/$",
        studyus.studyuser.views.ResearcherSignupView.as_view(),
        name="account_signup_researcher"),
    url(r"^account/signup/participant/$",
        studyus.studyuser.views.ParticipantSignupView.as_view(),
        name="account_signup_participant"),
    url(r"^account/", include("account.urls")),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='pages/home.html'),
        name='home')
)
