# Generated by Django 3.2 on 2021-04-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210423_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]