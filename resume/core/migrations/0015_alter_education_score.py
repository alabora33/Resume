# Generated by Django 4.2.3 on 2023-07-11 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_education_file_education_logos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='score',
            field=models.FloatField(blank=True, default='', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Score'),
        ),
    ]
