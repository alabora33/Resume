# Generated by Django 4.2.3 on 2023-07-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_education_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='images',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image'),
        ),
    ]
