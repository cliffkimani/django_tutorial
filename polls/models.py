from django.db import models

# Create your models here.

class Poll(models.Model):
    question = forms.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = forms.CharField(max_length=200)
    votes = models.IntegerField(default=0)

