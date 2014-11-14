from django.db import models

from django.contrib.auth.models import User


class StudyUserResearcher(models.Model):
    """A researcher user.

    fields:
        user: OneToOne, to Django User model
    """
    user = models.OneToOneField(User)


class StudyUserParticipant(models.Model):
    """A study participant.

    fields:
        user: OneToOne, to Django User model
        is_enrolled: Boolean, default is False
    """
    user = models.OneToOneField(User)
    is_enrolled = models.BooleanField(default=False)
