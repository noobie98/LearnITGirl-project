# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	user = models.ForeignKey(User)
	category= models.CharField(max_length=100)

	def __str__(self):
		return '%s %s'%(self.user,self.category)

class UserBookmark(models.Model):
	user = models.ForeignKey(User)
	bookmark = models.URLField()
	tag = models.CharField(max_length = 100)

	def __str__(self):
		return '%s %s'%(self.user,self.bookmark)