from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.
class Score(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    ban=models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username

class level(models.Model):
    l_number = models.IntegerField()
    numuser = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)
    wrong = models.IntegerField(default=0)


    def __unicode__(self):
        return self.text


class Answer(models.Model):
    answer = models.CharField(max_length=255)


class AnswerChecker(models.Model):
    index = models.PositiveIntegerField(default=0, unique=True)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

    def ans_value(self):
        return self.answer