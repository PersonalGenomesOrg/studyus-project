"""Default settings for the studyus.studyuser app.

STUDYUS_STUDYUSER_GEN_USER_ID:
  Default: Function that generates a random string of integers. Length of this
  string is defined by a single integer argument passed to the function.
STUDYUS_STUDYUSER_USER_ID_LEN:
  Default: 10

"""
import random
import string

from django.conf import settings


STUDYUS_STUDYUSER_GEN_USER_ID = getattr(
    settings,
    'STUDYUS_STUDYUSER_GEN_USER_ID',
    lambda x: ''.join(random.choice(string.digits) for _ in range(x)))

STUDYUS_STUDYUSER_USER_ID_LEN = getattr(
    settings,
    'STUDYUS_STUDYUSER_USER_ID_LEN',
    10)
