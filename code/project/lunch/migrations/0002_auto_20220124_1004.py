# Generated by Django 3.2.11 on 2022-01-24 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_id',
            new_name='user',
        ),
    ]
