# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.
from django.db import models

class Album(models.Model):
	artist=models.CharField(max_length=250)
	album_title=models.CharField(max_length=500)
	gener=models.CharField(max_length=100)
	album_logo=models.CharField(max_length=1000)
	#String Representation of object
	def __str__(self):
		return self.album_title+"-"+self.artist

class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)

	def __str__(self):
		return self.song_title