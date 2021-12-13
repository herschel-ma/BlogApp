from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Avatar(models.Model):
    content = models.ImageField(upload_to="avatar/%Y%m%d")


class userModel(AbstractUser):
    avatar = models.ForeignKey(Avatar,
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               related_name="user",
                               default=None)
    description = models.CharField(max_length=250,
                                   blank=True,
                                   null=True,
                                   default="")
