# Generated by Django 3.2.7 on 2021-10-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20211005_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='square',
            name='obstacle',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
