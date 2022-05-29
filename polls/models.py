import datetime

from django.db import models
from django.utils import timezone

class Question_2(models.Model):
    # 채점을 위해 answer 컬럼 추가 
    answer = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question_2, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
      return self.choice_text