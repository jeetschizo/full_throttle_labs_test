from django.db import models

# Create your models here.


class Word(models.Model):

    text = models.CharField(max_length=30)
    occurence = models.IntegerField()

    class Meta:
        app_label = 'words'
