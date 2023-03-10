# Generated by Django 3.2.17 on 2023-02-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headercontacts',
            name='bot_bph',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Бот ВРН'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='bot_msk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Бот Мск'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='bot_peter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Бот Спб'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='moscow',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Москва'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='operator_bph',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Оператор ВРН'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='operator_msk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Оператор Мск'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='operator_peter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Оператор Спб'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='peter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Питер'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='sup_bph',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тех Поддержка ВРН'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='sup_msk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тех Поддержка Мск'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='sup_peter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тех Поддержка Спб'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='visitka_msk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Визитка Мск'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='visitka_peter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Визитка Спб'),
        ),
        migrations.AlterField(
            model_name='headercontacts',
            name='voronezh',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Воронеж'),
        ),
    ]
