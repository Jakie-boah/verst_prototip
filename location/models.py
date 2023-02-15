from django.db import models
from items.models import TestItemModel

# Create your models here.


class Locations(models.Model):
    item = models.ForeignKey(TestItemModel, on_delete=models.CASCADE, verbose_name='Товар')
    location = models.CharField(verbose_name='Локация', max_length=50)
