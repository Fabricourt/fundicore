# Generated by Django 2.2.2 on 2019-06-27 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundi', '0006_auto_20190627_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundi',
            old_name='title',
            new_name='skill',
        ),
    ]