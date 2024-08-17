from django.db import models

# Create your models here.
class Company (models.Model):
    name = models.CharField('Nombre', max_length=100)

    def __str__(self):
        return f'{self.name}'