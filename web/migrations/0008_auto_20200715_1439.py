# Generated by Django 3.0.8 on 2020-07-15 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200715_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='file',
            new_name='img',
        ),
    ]
