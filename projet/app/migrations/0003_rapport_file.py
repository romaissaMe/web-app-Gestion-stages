# Generated by Django 4.0.1 on 2022-02-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_rapport_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='rapport',
            name='file',
            field=models.FileField(null=True, upload_to='media/rapports'),
        ),
    ]
