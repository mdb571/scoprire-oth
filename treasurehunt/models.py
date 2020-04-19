from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.
class Score(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username


class Answer(models.Model):
    answer = models.CharField(max_length=255)


class AnswerChecker(models.Model):
    index = models.PositiveIntegerField(default=0, unique=True)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

    def ans_value(self):
        return self.answer