from cities.models import City
from django.db import models
# Create your models here.


class TestItemModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
