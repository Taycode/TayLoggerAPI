from django.db import models


class LogGroup(models.Model):
    name = models.CharField(max_length=30)


class Log(models.Model):
    group = models.ForeignKey(LogGroup, models.DO_NOTHING)
    message = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
