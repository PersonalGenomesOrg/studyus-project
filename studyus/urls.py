from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',

    url(r'^studyuser/', include('studyus.studyuser.urls')),
)
