# Generated by Django 2.2 on 2019-07-14 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('autochart', '0002_remove_userfile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='file',
        ),
        migrations.AddField(
            model_name='userfile',
            name='session_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfile',
            name='user_id',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
