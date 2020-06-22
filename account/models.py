from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string


def generate_key(model_field, model, prefix=""):

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
    if sender and kwargs["created"]:
        instance = kwargs["instance"]
        instance.public_key = generate_key("public_key", User, "PUB")
        instance.secret_key = generate_key("secret_key", User, "SEC")
        instance.save()
        return None

post_save.connect(create_keys_for_user, User)
