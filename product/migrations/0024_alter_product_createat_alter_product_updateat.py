# Generated by Django 5.0.1 on 2024-02-06 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_product_createat_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='createat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 53, 56, 57634, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updateat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 13, 53, 56, 57634, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
