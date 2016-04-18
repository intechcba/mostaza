from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group

DEFAULT_CHAR_VALUE = 'Unknown'
ADMIN_GROUP = 'Admin'


class UserManager(BaseUserManager):

    def create_user(self, username, email, groups, password=None):
        if not username:
            raise ValueError('Users must have username')

        user = self.model(
            username=username,
            email=email,
            state=self.model(
                id=1,
                state='confirmed'
            )
        )
        user.set_password(password)
        user_groups = {}
        for group in groups:
            user_groups.add(Group.objects.get(name=group))
        user.groups = user_groups
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, ADMIN_GROUP, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class UserState(models.Model):
    description = models.CharField(max_length=20)

class User(AbstractUser):
    state = models.ForeignKey(UserState, on_delete=models.DO_NOTHING)
    object = UserManager()

class Doctor(models.Model):
    first_name = models.CharField(max_length=100, null=False, default=DEFAULT_CHAR_VALUE)
    last_name = models.CharField(max_length=100, null=False, default=DEFAULT_CHAR_VALUE)
    address = models.CharField(max_length=200, null=False, default=DEFAULT_CHAR_VALUE)
    phone_number = models.CharField(max_length=20, null=False, default=DEFAULT_CHAR_VALUE)
    reg_number = models.CharField(max_length=20, null=False, default=DEFAULT_CHAR_VALUE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

