# Generated by Django 2.2 on 2019-07-14 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autochart', '0004_auto_20190714_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='user_id',
        ),
    ]
