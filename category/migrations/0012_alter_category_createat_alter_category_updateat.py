# Generated by Django 5.0.1 on 2024-02-06 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_alter_category_createat_alter_category_updateat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='createat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 8, 50, 55, 540357, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updateat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 8, 50, 55, 540357, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]