from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220,)
	# shortcode = models.CharField()
	# shortcode = models.CharField(max_length=15) default values for null=False, blank=False
	shortcode = models.CharField(max_length=15, default='ABCD', unique=True)

	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	empty_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)


	
	def __str__(self):
		return str(self.url)

	# For python 2
	def __unicode__(self):
		return str(self.url)