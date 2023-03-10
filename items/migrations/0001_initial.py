# Generated by Django 3.2.17 on 2023-02-15 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cities.city')),
            ],
        ),
    ]
