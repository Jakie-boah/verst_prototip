from django.db import models

# Create your models here.


class MoscowContacts(models.Model):
    bot_1 = models.URLField(max_length=200, verbose_name='Бот Распределитель 1', blank=True, null=True)
    bot_2 = models.URLField(max_length=200, verbose_name='Бот Распределитель 2', blank=True, null=True)
    bot_3 = models.URLField(max_length=200, verbose_name='Бот Распределитель 3', blank=True, null=True)
    bot_4 = models.URLField(max_length=200, verbose_name='Бот Распределитель 4', blank=True, null=True)
    bot_5 = models.URLField(max_length=200, verbose_name='Бот Распределитель 5', blank=True, null=True)
    ac_bot = models.URLField(max_length=200, verbose_name='Аккаунт-Бот Москва/Питер', blank=True, null=True)
    bot = models.URLField(max_length=200, verbose_name='Бот Москва/Питер Айклад', blank=True, null=True)
    hand_sell = models.URLField(max_length=200, verbose_name='Ручные продажи', blank=True, null=True)
    tech_sup = models.URLField(max_length=200, verbose_name='Тех.Поддержка', blank=True, null=True)
    employ_qs = models.URLField(max_length=200, verbose_name='По вопросам устройства', blank=True, null=True)

    def __str__(self):
        return 'Ссылки во вкладке Контакты для Москвы'

    class Meta:
        verbose_name = 'Контакты Москва'
        verbose_name_plural = 'Контакты Москва'


class PeterContacts(models.Model):
    bot_1 = models.URLField(max_length=200, verbose_name='Бот Распределитель 1', blank=True, null=True)
    bot_2 = models.URLField(max_length=200, verbose_name='Бот Распределитель 2', blank=True, null=True)
    bot_3 = models.URLField(max_length=200, verbose_name='Бот Распределитель 3', blank=True, null=True)
    bot_4 = models.URLField(max_length=200, verbose_name='Бот Распределитель 4', blank=True, null=True)
    bot_5 = models.URLField(max_length=200, verbose_name='Бот Распределитель 5', blank=True, null=True)
    ac_bot = models.URLField(max_length=200, verbose_name='Аккаунт-Бот Москва/Питер', blank=True, null=True)
    bot = models.URLField(max_length=200, verbose_name='Бот Москва/Питер Айклад', blank=True, null=True)
    hand_sell = models.URLField(max_length=200, verbose_name='Ручные продажи', blank=True, null=True)
    tech_sup = models.URLField(max_length=200, verbose_name='Тех.Поддержка', blank=True, null=True)
    employ_qs = models.URLField(max_length=200, verbose_name='По вопросам устройства', blank=True, null=True)

    def __str__(self):
        return 'Ссылки во вкладке Контакты для Питера'

    class Meta:
        verbose_name = 'Контакты Питер'
        verbose_name_plural = 'Контакты Питер'


class VoronezhContacts(models.Model):
    bot_1 = models.URLField(max_length=200, verbose_name='Бот 1', blank=True, null=True)
    bot = models.URLField(max_length=200, verbose_name='Бот Воронеж Айклад', blank=True, null=True)
    hand_sell = models.URLField(max_length=200, verbose_name='Ручные продажи', blank=True, null=True)
    tech_sup = models.URLField(max_length=200, verbose_name='Тех.Поддержка', blank=True, null=True)
    employ_qs = models.URLField(max_length=200, verbose_name='По вопросам устройства', blank=True, null=True)

    def __str__(self):
        return 'Ссылки во вкладке Контакты для Воронежа'

    class Meta:
        verbose_name = 'Контакты Воронеж'
        verbose_name_plural = 'Контакты Воронеж'


class RestOfContacts(models.Model):
    our_site = models.URLField(max_length=200, verbose_name='Наш сайт', blank=True, null=True)
    contacts_site = models.URLField(max_length=200, verbose_name='Сайт с контактами', blank=True, null=True)
    site_chips = models.URLField(max_length=200, verbose_name='Сайт чипсы', blank=True, null=True)

    def __str__(self):
        return 'Все остальные ссылки во вкладке Контакты'

    class Meta:
        verbose_name = 'Оставшиеся ссылки'
        verbose_name_plural = 'Оставшиеся ссылки'
