from django.db import models
from users.models import *
from ckeditor.fields import RichTextField

def image_directory_path(instance, filename):
    title = slugify(instance.title)
    _, extension = os.path.splitext(filename)
    return f"Images/{title}{extension}"

class Project(models.Model):
	user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
	title = models.TextField(max_length=100)
	project_type = models.ForeignKey('Project_Type', on_delete=models.CASCADE, null=False)
	home = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Project_Type(models.Model):
	title = models.TextField(max_length=100, unique=True)

	def __str__(self):
		return self.title

class Page(models.Model):
	project_id = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)
	title = models.TextField(max_length=100)
	active = models.BooleanField(unique=False)

	def __str__(self):
		return self.title

class Section(models.Model):
	page_id = models.ForeignKey('Page', on_delete=models.CASCADE, null=False)
	title = models.TextField(max_length=100)
	order = models.IntegerField(blank=True)

	def __str__(self):
		return self.title

class Section_Image(models.Model):
	section_id = models.ForeignKey('Section', on_delete=models.CASCADE, null=False)
	image_id = models.ForeignKey('Image', on_delete=models.CASCADE, null=False)
	order = models.IntegerField(blank=True)
	is_background = models.BooleanField(default=False)

class Logo_Image(models.Model):
	project_id= models.ForeignKey('Project', on_delete=models.CASCADE)
	image_id= models.ForeignKey('Image', on_delete=models.CASCADE)
	title = models.TextField(max_length=100)


class Image(models.Model):
	user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
	title = models.TextField(max_length=100)
	image = models.ImageField(
		upload_to=image_directory_path, blank=True
	)
	def __str__(self):
		return self.title


class Section_Text(models.Model):
	section_id = models.ForeignKey('Section', on_delete=models.CASCADE, null=False)
	text_id = models.ForeignKey('Text', on_delete=models.CASCADE, null=False)
	order = models.IntegerField(blank=True)

class Text(models.Model):
	title = models.TextField(max_length=100)
	text = RichTextField(config_name='awesome_ckeditor')
	font = models.TextField(max_length=100)
	font_size = models.TextField(max_length=100)
	font_weight = models.TextField(max_length=100)

	def __str__(self):
		return self.title

class Section_Link(models.Model):
	section_id = models.ForeignKey('Section', on_delete=models.CASCADE, null=False)
	link_id = models.ForeignKey('Link', on_delete=models.CASCADE, null=False)
	order = models.IntegerField(blank=True)


class Social_Media_Link(models.Model):
	title = models.TextField(max_length=100)
	project_id = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)
	image_id = models.ForeignKey('Image', on_delete=models.CASCADE, null=False)
	link_id = models.ForeignKey('Link', on_delete=models.CASCADE, null=False)
	order = models.IntegerField(blank=True)


class Link(models.Model):
	title = models.TextField(max_length=100)
	text = models.TextField(max_length=100)

	def __str__(self):
		return self.title
