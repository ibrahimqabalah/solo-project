# Generated by Django 2.2.4 on 2023-12-22 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0002_auto_20231220_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='update',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='created',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='update',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='created',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='update',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='created',
            new_name='updated_at',
        ),
    ]
