# Generated by Django 3.2.17 on 2023-02-15 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testitemmodel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city'),
        ),
    ]
