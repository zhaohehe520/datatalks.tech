# Generated by Django 2.2 on 2019-07-09 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autochart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='image',
        ),
    ]
