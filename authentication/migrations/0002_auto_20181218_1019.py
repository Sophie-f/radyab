# Generated by Django 2.1.4 on 2018-12-18 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sex',
            new_name='gender',
        ),
    ]