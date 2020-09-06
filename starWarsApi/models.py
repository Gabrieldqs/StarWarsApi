from django.db import models 

class Planet(models.Model):
	name = models.CharField(max_length=100)
	climate = models.CharField(max_length=100)
	terrain = models.CharField(max_length=100)
	films = models.IntegerField()