# Generated by Django 3.2 on 2021-04-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_foodorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodorder',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
