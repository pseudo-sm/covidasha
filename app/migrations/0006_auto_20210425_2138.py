# Generated by Django 3.2 on 2021-04-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_alert_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='money',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alert',
            name='others',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alert',
            name='oxygen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alert',
            name='plasma',
            field=models.BooleanField(default=False),
        ),
    ]
