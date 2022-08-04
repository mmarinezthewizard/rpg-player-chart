from django.db import models

# Create your models here.
class PlayerModel(models.Model):
    name =  models.CharField(max_length=30)
    player_class = models.CharField(max_length=30)
    strength = models.CharField(max_length=30)
    intelligence = models.CharField(max_length=30)
    faith = models.CharField(max_length=30)
    dexterity = models.CharField(max_length=30)
    vigor = models.CharField(max_length=30)
    
