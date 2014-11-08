from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

import studyus.studyuser.views

urlpatterns = patterns(
    '',

    # Override required for some default django-user-accounts urls.
    url(r"^account/signup/$", studyus.studyuser.views.SignupView.as_view(),
        name="account_signup"),
    # url(r"^account/login/$", studyus.studyuser.LoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),

    url(r'^studyus/', include('studyus.urls', namespace='studyus')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'))
)
