# Generated by Django 5.0.1 on 2024-02-06 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_alter_category_createat_alter_category_updateat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='createat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 1, 23, 10, 6773, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updateat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 1, 23, 10, 6773, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
