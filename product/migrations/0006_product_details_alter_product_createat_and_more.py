# Generated by Django 5.0.1 on 2024-02-03 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_age_alter_product_createat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='createat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 20, 46, 58, 34495, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updateat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 20, 46, 58, 34495, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
