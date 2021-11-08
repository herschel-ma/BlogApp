from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from users.models import userModel


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(userModel, related_name='user', on_delete=models.CASCADE,)
    nickname = models.CharField(max_length=20)
    avatar_url = models.TextField(
        max_length=255,
        default='https://source.unsplash.com/collection/1346951/50x50?sig=1')
    github_node_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nickname
