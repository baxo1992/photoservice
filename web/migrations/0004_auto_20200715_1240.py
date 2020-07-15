# Generated by Django 3.0.8 on 2020-07-15 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('web', '0003_auto_20200715_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile'),
        ),
    ]
