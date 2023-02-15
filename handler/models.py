from django.db import models

# Create your models here.


class HeaderContacts(models.Model):
    moscow = models.URLField(max_length=200, verbose_name='Москва', blank=True, null=True)
    peter = models.URLField(max_length=200, verbose_name='Питер', blank=True, null=True)
    voronezh = models.URLField(max_length=200, verbose_name='Воронеж', blank=True, null=True)

    bot_msk = models.URLField(max_length=200, verbose_name='Бот Мск', blank=True, null=True)
    operator_msk = models.URLField(max_length=200, verbose_name='Оператор Мск', blank=True, null=True)
    sup_msk = models.URLField(max_length=200, verbose_name='Тех Поддержка Мск', blank=True, null=True)
    visitka_msk = models.URLField(max_length=200, verbose_name='Визитка Мск', blank=True, null=True)

    bot_peter = models.URLField(max_length=200, verbose_name='Бот Спб', blank=True, null=True)
    operator_peter = models.URLField(max_length=200, verbose_name='Оператор Спб', blank=True, null=True)
    sup_peter = models.URLField(max_length=200, verbose_name='Тех Поддержка Спб', blank=True, null=True)
    visitka_peter = models.URLField(max_length=200, verbose_name='Визитка Спб', blank=True, null=True)

    bot_bph = models.URLField(max_length=200, verbose_name='Бот ВРН', blank=True, null=True)
    operator_bph = models.URLField(max_length=200, verbose_name='Оператор ВРН', blank=True, null=True)
    sup_bph = models.URLField(max_length=200, verbose_name='Тех Поддержка ВРН', blank=True, null=True)

    def __str__(self):
        return 'Ссылки головы'

    class Meta:
        verbose_name = 'Ссылки головы'
        verbose_name_plural = 'Ссылки головы'
