# Generated by Django 3.2.11 on 2022-01-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0004_alter_menurecipe_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='menurecipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='menurecipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
