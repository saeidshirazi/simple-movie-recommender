from __future__ import unicode_literals

from django.db import models

# Create your models here.

class movies(models.Model):
	movie_id = models.IntegerField(default=0)
	imdb_id = models.IntegerField(default=0)
	movie_name = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	vectors = models.CharField(max_length=20)

class meansize(models.Model):
	movie_id = models.IntegerField(default=0)
	size = models.FloatField(default=0.0)
	mean = models.FloatField(default=0.0) #miangin

class links(models.Model):
	movie_id = models.IntegerField(default=0)
	url = models.CharField(max_length=300)
