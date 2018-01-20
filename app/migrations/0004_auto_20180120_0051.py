# Generated by Django 2.0.1 on 2018-01-20 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180120_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]*$')], verbose_name='Telefone'),
        ),
    ]
