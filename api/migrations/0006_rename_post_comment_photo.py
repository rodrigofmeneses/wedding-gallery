# Generated by Django 4.2.4 on 2023-08-04 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_like_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='photo',
        ),
    ]
