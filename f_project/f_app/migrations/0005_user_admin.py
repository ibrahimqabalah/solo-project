# Generated by Django 2.2.4 on 2023-12-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0004_remove_product_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
