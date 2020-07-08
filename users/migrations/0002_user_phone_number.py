# Generated by Django 3.0.8 on 2020-07-07 20:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Numer telefonu powinnien posiadać od 9 do 15 cyfr!', regex='^\\d{9,15}$')]),
        ),
    ]