from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from datetime import datetime
from django_hosts import reverse

from .utils import create_shortcode


# SHORT_CODE_MAX_LENGTH = settings.SHORT_CODE_MAX_LENGTH

# It's better to use following because of few reasons: Reusable Application 
# [15 is the default value if not set in properties]
SHORT_CODE_MAX_LENGTH = getattr(settings, "SHORT_CODE_MAX_LENGTH", 15)

class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_original = super(KirrURLManager, self).all(*args, **kwargs)
		qs_customized = qs_original.filter(active=True)
		return qs_customized


	def refresh_shortcodes(self, lastX = 100):
		qs = KirrURL.objects.filter(id__gte=1) # signifies id >=1
		# qs = KirrURL.objects.filter(id>=1) # signifies id >=1 wouldn't work (says sth like bool is not iterable)

		if lastX is not None and isinstance(lastX, int):
			qs = qs.order_by('-id')[:lastX] # this would make it in descending order of id 
			# (to change the default ordering of query set, add class Meta inside KirrURL)

		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id, q.shortcode)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)


# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220,)
	# shortcode = models.CharField()
	# shortcode = models.CharField(max_length=15) default values for null=False, blank=False
	shortcode = models.CharField(max_length=SHORT_CODE_MAX_LENGTH, blank=True, unique=True)

	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	empty_timestamp = models.DateTimeField(default=datetime.now())
	active 			= models.BooleanField(default=True)

	objects = KirrURLManager() # to attach our custom models.Manager to our Model

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == '':
			self.shortcode = create_shortcode(self)
		super(KirrURL, self).save(*args, **kwargs)

	
	def __str__(self):
		return str(self.url)

	# For python 2
	def __unicode__(self):
		return str(self.url)

	# class Meta:
	# 	ordering = '-id'

	def get_shortcode(self):
		# It works just fine but it's hard coding, better use django-hosts reverse method
		hardcoded_url_return = "http://www.reviewsandnotes.space:8000/{shortcode}".format(shortcode=self.shortcode)
		url_return = hardcoded_url_return

		# TODO: Reverse functionalizty needs to be implemented (It's not working right now)!
		# generalized_url_return = reverse('shortcode_url', kwargs={'shortcode': self.shortcode})
		# generalized_url_return = reverse('shortcode_url', host='www_name_123', port='8000', scheme='http', kwargs={'shortcode': self.shortcode})
		# url_return = generalized_url_return

		return url_return