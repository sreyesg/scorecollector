from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Score(models.Model):
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    page = models.IntegerField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('score-detail', kwargs={'score_id': self.id})
    
            
# Create your models here.
