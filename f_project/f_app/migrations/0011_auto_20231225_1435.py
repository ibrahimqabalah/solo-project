# Generated by Django 2.2.4 on 2023-12-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0010_auto_20231225_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='product_price',
            field=models.IntegerField(default=10),
        ),
    ]