# Generated by Django 2.1 on 2019-02-24 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0006_auto_20190203_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]