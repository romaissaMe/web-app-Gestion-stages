# Generated by Django 4.0.1 on 2022-02-10 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rapport',
            name='file',
        ),
    ]
