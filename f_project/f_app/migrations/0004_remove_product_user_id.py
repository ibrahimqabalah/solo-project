# Generated by Django 2.2.4 on 2023-12-22 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0003_auto_20231222_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_id',
        ),
    ]
