from django.db import models
from pages.models import *

class Navbar(models.Model):
	project_id = models.ForeignKey('pages.Project', on_delete=models.CASCADE, null=True)
	title = models.TextField(max_length=100)
	navbar_type = models.ForeignKey('Navbar_Type', on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.title

class Navbar_Type(models.Model):
	title = models.TextField(max_length=100, unique=True)

	def __str__(self):
		return self.title
