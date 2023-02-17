from django.db import models

# Create your models here.


class SalesContacts(models.Model):
    op_hand_sell = models.URLField(max_length=200, verbose_name='Оператор ручных продаж', blank=True, null=True)
    photo_link = models.URLField(max_length=200, verbose_name='Ссылка на фото', blank=True, null=True)
    operator = models.URLField(max_length=200, verbose_name='Оператор', blank=True, null=True)

    def __str__(self):
        return 'Ссылки во вкладке Акции'

    class Meta:
        verbose_name = 'Контакты Акции'
        verbose_name_plural = 'Контакты Акции'
