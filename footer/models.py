from django.db import models
from pages.models import *

class Footer(models.Model):
	project_id = models.ForeignKey('pages.Project', on_delete=models.CASCADE, null=True)
	title = models.TextField(max_length=100)
	footer_type = models.ForeignKey('Footer_Type', on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.title

class Footer_Type(models.Model):
	title = models.TextField(max_length=100, unique=True)

	def __str__(self):
		return self.title
