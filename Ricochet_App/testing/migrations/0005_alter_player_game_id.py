# Generated by Django 3.2.7 on 2021-09-29 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_alter_player_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='game_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testing.game'),
        ),
    ]