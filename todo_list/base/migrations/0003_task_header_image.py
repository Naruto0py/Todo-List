# Generated by Django 4.1 on 2022-08-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_descriptio_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]