# Generated by Django 2.2 on 2019-07-14 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autochart', '0006_auto_20190714_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='session_time',
            field=models.DecimalField(decimal_places=10, max_digits=31),
        ),
    ]