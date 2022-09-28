from django.db import models

# Create your models here.
class Question(models.Model):
    questionID = models.IntegerField(primary_key=True)
    passageID = models.IntegerField()
    question_type = models.IntegerField()
    question = models.TextField(max_length=1000)
    new_passage = models.TextField(max_length=2000)
    answer = models.TextField(max_length=100)
    d1 = models.TextField(max_length=100)
    d2 = models.TextField(max_length=100)
    d3 = models.TextField(max_length=100)
    d4 = models.TextField(max_length=100)

    class Meta:
      db_table = 'question'