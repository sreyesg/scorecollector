from django.db import models
from django.urls import reverse

class Score(models.Model):
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    page = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('score-detail', kwargs={'score_id': self.id})
    
        
# Create your models here.
