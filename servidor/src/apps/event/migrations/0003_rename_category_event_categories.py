# Generated by Django 3.2.20 on 2023-08-29 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20230829_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Category',
            new_name='categories',
        ),
    ]