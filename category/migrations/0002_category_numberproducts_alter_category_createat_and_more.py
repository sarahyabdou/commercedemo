# Generated by Django 5.0.1 on 2024-02-03 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='numberproducts',
            field=models.IntegerField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='createat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 21, 0, 47, 603020, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updateat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 21, 0, 47, 603020, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
