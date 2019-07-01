# Generated by Django 2.2.2 on 2019-06-26 05:38

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('fafa', models.CharField(max_length=100, null=True)),
                ('statements', ckeditor.fields.RichTextField(blank=True, max_length=400, null=True)),
                ('reload', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
