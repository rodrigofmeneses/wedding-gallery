# Generated by Django 4.2.4 on 2023-08-04 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_photo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='post',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='content',
        ),
    ]