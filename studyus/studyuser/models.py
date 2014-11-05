from django.db import models

from django.contrib.auth.models import User

from .settings_default import (STUDYUS_STUDYUSER_GEN_USER_ID as GEN_USER_ID,
                               STUDYUS_STUDYUSER_USER_ID_LEN as USER_ID_LEN)


class StudyUser(models.Model):
    """Abstract base class for users in studyus app.

    StudyUsers effectively has two attributes:
     - an email (email)
     - a unique, randomly generated identifier (user_id)

    These are stored in the corresponding User's email and username fields,
    but can be called as attributes in StudyUser itself.
    """
    # TODO notes:
    # Consider supporting names, but make sure this is optional on ALL levels.
    # Consider optional postal addresses, but globalization is an issue.
    # Consider optional arbitrary study-assigned IDs.
    # Consider optional user designated handles (usernames).

    user = models.OneToOneField(User)

    class Meta:
        abstract = True

    @classmethod
    def create(cls, email):
        username = cls._get_user_id()
        user = User(username=username, email=email)
        user.save()
        return cls(user=user)

    @property
    def email(self):
        return self.user.email

    @property
    def random_id(self):
        return self.user.username

    @classmethod
    def _get_user_id(cls):
        """Calls generate_user_id until a unique ID is created."""
        user_id = cls.generate_user_id()
        while cls.objects.filter(user_id=user_id):
            user_id = cls.generate_user_id()
        return user_id

    @staticmethod
    def generate_user_id():
        """Default settings generates a random 10 digit string.

        STUDYUS_STUDYUSER_USER_ID_LEN can be set as an int to change the length
        STUDYUS_STUDYUSER_GEN_USER_ID can be set as a zero-argument lambda to
            create a custom random user ID.
        """
        try:
            return GEN_USER_ID(USER_ID_LEN)
        except TypeError:
            try:
                return GEN_USER_ID()
            except TypeError:
                msg = ("STUDYUS_STUDYUSER_GEN_USER_ID must be a function " +
                       "that expects either one argument (an int defined by " +
                       "STUDYUS_STUDYUSER_USER_ID_LEN) or no arguments.")
                raise TypeError(msg)


class StudyParticipant(StudyUser):
    """A StudyUser representing a participant."""
    enrolled = models.BooleanField(default=False)


class StudyAdmin(StudyUser):
    """A StudyUser representing a study administrator.

    The StudyAdmin is_admin field defaults to "False" upon account creation,
    and must be set to "True" by a site administrator.
    """
    is_admin = models.BooleanField(default=False)
