# Generated by Django 3.2.17 on 2023-02-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_hand_sell', models.URLField(blank=True, null=True, verbose_name='Оператор ручных продаж')),
                ('photo_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на фото')),
                ('operator', models.URLField(blank=True, null=True, verbose_name='Оператор')),
            ],
            options={
                'verbose_name': 'Контакты Акции',
                'verbose_name_plural': 'Контакты Акции',
            },
        ),
    ]
