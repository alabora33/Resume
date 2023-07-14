# Generated by Django 4.2.3 on 2023-07-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_document_alter_socialmedia_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=254),
        ),
    ]
