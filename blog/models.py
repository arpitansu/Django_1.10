from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


class BlogPost(models.Model):
	title = models.CharField(max_length=64)
	writer = models.CharField(max_length=30)
	date = models.DateTimeField()
	body = HTMLField()

	def __str__(self):
		return "{} :-> {} -- {} -- {} -- {}" .format(self.id, self.title, self.writer,self.body, self.date)

