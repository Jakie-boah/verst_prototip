# Generated by Django 3.2.17 on 2023-02-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0004_auto_20230215_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moscow', models.URLField(blank=True, null=True, verbose_name='Москва')),
                ('peter', models.URLField(blank=True, null=True, verbose_name='Питер')),
                ('voronezh', models.URLField(blank=True, null=True, verbose_name='Воронеж')),
            ],
            options={
                'verbose_name': 'Вакансии',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
