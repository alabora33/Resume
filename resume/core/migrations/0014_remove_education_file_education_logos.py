# Generated by Django 4.2.3 on 2023-07-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_education_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='file',
        ),
        migrations.AddField(
            model_name='education',
            name='logos',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image'),
        ),
    ]
