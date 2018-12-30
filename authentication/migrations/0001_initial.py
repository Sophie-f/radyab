# Generated by Django 2.1.4 on 2018-12-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('f_name', models.CharField(max_length=512)),
                ('age', models.IntegerField(default=25, null=True)),
                ('sex', models.BooleanField(default=True)),
            ],
        ),
    ]