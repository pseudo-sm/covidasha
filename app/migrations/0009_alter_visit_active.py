# Generated by Django 3.2 on 2021-04-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_visit_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
