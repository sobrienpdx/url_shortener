# Generated by Django 2.0 on 2018-08-13 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Short_Cut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.TextField(unique=True)),
                ('shortcut', models.TextField(unique=True)),
                ('created_Date', models.DateTimeField(default=datetime.datetime(2018, 8, 13, 18, 45, 5, 56996))),
            ],
        ),
    ]
