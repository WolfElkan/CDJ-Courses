from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
	course_name = models.CharField(max_length= 45)
	description = models.TextField(max_length=200)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "\n[{}] {}".format(self.id, self.course_name)