from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LogGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username + " - " + self.name


class Log(models.Model):
    group = models.ForeignKey(LogGroup, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.message[:30]} ({self.group.name}) - {self.time}'
