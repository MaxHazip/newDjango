from django.db import models

# Create your models here.
class Books(models.Model):
    name =  models.CharField('Название книги', max_length=35, unique=True)
    year = models.DateField("Дата издания", default='2025-01-01')
    author = models.ManyToManyField('Authors')

class Authors(models.Model):
    name =  models.CharField('Имя автора', max_length=35, unique=True)