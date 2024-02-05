# Generated by Django 5.0.1 on 2024-02-05 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_createat_alter_product_updateat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='createat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 0, 21, 47, 155378, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updateat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 0, 21, 47, 155378, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]