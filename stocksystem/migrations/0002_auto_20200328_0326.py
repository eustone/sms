# Generated by Django 3.0.4 on 2020-03-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventory'},
        ),
        migrations.AlterField(
            model_name='author',
            name='dob',
            field=models.DateField(),
        ),
    ]
