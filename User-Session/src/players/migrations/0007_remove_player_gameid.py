# Generated by Django 5.1.2 on 2024-12-17 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0006_matchplayer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="GameId",
        ),
    ]