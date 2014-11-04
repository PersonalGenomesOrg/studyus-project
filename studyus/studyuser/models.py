from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

from .. import settings_defaults as studyuser_defaults

# Import this default specifically so we can check if it's been overridden.
from ..settings_defaults import DEFAULT_STUDYUS_STUDYUSER_GEN_USER_ID

settings.configure(default_settings=studyuser_defaults)


class StudyUser(models.Model):
    """Abstract base class for users in studyus app.

    StudyUsers effectively has two attributes:
     - an email (email)
     - a unique, randomly generated identifier (user_id)

    These are stored in the corresponding User's email and username fields,
    but can be called as attributes in StudyUser itself.
    """

    user = models.OneToOneField(User)

    class Meta:
        abstract = True

    def __init__(self, email, *args, **kwargs):
        this_user = User(email=email,
                         username=self.generate_user_id())
        this_user.save()
        super(StudyUser, self).__init__(user=this_user, *args, **kwargs)

    @property
    def email(self):
        return self.user.email

    @property
    def user_id(self):
        return self.user.username

    @classmethod
    def _get_user_id(cls):
        """Calls generate_user_id until a unique ID is created."""
        user_id = cls.generate_user_id()
        while cls.objects.filter(user_id=user_id):
            user_id = cls.generate_user_id()

    @staticmethod
    def generate_user_id():
        """Default settings generates a random 10 digit string.

        STUDYUS_STUDYUSER_USER_ID_LEN can be set as an int to change the length
        STUDYUS_STUDYUSER_GEN_USER_ID can be set as a zero-argument lambda to
            create a custom random user ID.
        """
        gen_user_id_fun = settings['STUDYUS_STUDYUSER_GEN_USER_ID']
        if gen_user_id_fun == DEFAULT_STUDYUS_STUDYUSER_GEN_USER_ID:
            return gen_user_id_fun(settings['STUDYUS_STUDYUSER_USER_ID_LEN'])
        else:
            return gen_user_id_fun()


class StudyParticipant(StudyUser):
    """A StudyUser representing a participant."""
    enrolled = models.BooleanField(default=False)


class StudyAdmin(StudyUser):
    """A StudyUser representing a study administrator."""
    is_admin = True
