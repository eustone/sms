# Generated by Django 3.0.4 on 2020-04-25 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200425_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='telephone_number_of_contact',
            field=models.CharField(blank=True, default='', max_length=12),
        ),
    ]