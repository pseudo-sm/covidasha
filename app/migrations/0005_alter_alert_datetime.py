# Generated by Django 3.2 on 2021-04-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_alert_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
