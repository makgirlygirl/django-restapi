from django.db import models

# Create your models here.

class Passage(models.Model):
    passageID = models.IntegerField(
      auto_created=True
    )

    passage = models.TextField(
      max_length=2000,
      null=False,
      blank=False
    )

    class Meta:
     db_table = 'passage'