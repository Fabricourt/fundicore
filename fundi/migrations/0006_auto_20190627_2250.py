# Generated by Django 2.2.2 on 2019-06-27 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundi', '0005_auto_20190627_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fundi',
            options={'ordering': ['-created_on']},
        ),
    ]