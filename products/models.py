from django.db import models
from ckeditor.fields import RichTextField
from pages.models import *


# Create your models here.
class Product(models.Model):
    project_id = models.ForeignKey('pages.Project', on_delete=models.CASCADE)
    image= models.ImageField(upload_to="products/")
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.IntegerField(default=0)
    supply= models.IntegerField(default=0)
    categories = models.ManyToManyField('Category', related_name='products', blank=True)
    terms_and_conditions = models.ForeignKey('Terms_And_Conditions', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    @property
    def in_stock(self):
        if self.supply > 0:
            return True
        else:
            return False



    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

class Terms_and_Conditions(models.Model):
    title = models.TextField(max_length=100)
    discription = RichTextField(config_name='awesome_ckeditor')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return self.title




