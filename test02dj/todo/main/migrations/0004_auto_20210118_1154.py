# Generated by Django 3.1.3 on 2021-01-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210118_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='Цена'),
        ),
    ]