"""Default settings for the studyus.studyuser app."""
import random
import string

from django.conf import settings

FOO = getattr(settings, 'FOO', "default_value")


STUDYUS_STUDYUSER_GEN_USER_ID = getattr(
    settings,
    'STUDYUS_STUDYUSER_GEN_USER_ID',
    lambda x: ''.join(random.choice(string.digits) for _ in range(x)))

STUDYUS_STUDYUSER_USER_ID_LEN = getattr(
    settings,
    'STUDYUS_STUDYUSER_USER_ID_LEN',
    10)

STUDYUS_STUDYUSER_SIGNUP_SUCC_URL = getattr(
    settings,
    'STUDYUS_STUDYUSER_SIGNUP_SUCC_URL',
    '/'
)

STUDYUS_STUDYUSER_LOGIN_SUCC_URL = getattr(
    settings,
    'STUDYUS_STUDYUSER_LOGIN_SUCC_URL',
    '/'
)
