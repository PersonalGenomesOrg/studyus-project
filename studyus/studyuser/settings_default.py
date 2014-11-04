"""Default settings for the studyus.studyuser app."""
import random
import string


STUDYUS_STUDYUSER_GEN_USER_ID = lambda x: ''.join(
    random.choice(string.digits) for _ in range(x))

STUDYUS_STUDYUSER_USER_ID_LEN = 10
