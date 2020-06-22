from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


def generate_key(model_field, model, prefix=""):
    """

    :param model_field:
    :param model:
    :param prefix:
    :return:
    """
    while True:
        key = f"{prefix}_{get_random_string(32)}"
        if model and model_field:
            data = {}
            data[model_field] = key
            if not model.objects.filter(**data):
                break

    return key


class User(AbstractUser):
    public_key = models.CharField(max_length=50)
    secret_key = models.CharField(max_length=50)

    def __str__(self):
        return self.username


def create_keys_for_user(sender, **kwargs):
    """

    :param sender:
    :param kwargs:
    :return:
    """
    if sender and kwargs["created"]:
        instance = kwargs["instance"]
        instance.public_key = generate_key("public_key", User, "PUB")
        instance.secret_key = generate_key("secret_key", User, "SEC")
        instance.save()
        return None


post_save.connect(create_keys_for_user, User)


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    """

    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if sender and created:
        Token.objects.create(user=instance)
        return None
