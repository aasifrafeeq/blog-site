# Generated by Django 2.2.1 on 2019-05-31 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='heading',
            new_name='h',
        ),
    ]
