# Generated by Django 5.1.2 on 2024-11-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=100)),
                ('maxAmountOfPlayers', models.IntegerField(default=2)),
                ('amountOfPlayers', models.IntegerField(default=1)),
                ('type', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('privateRoom', models.BooleanField(default=False)),
                ('createdBy', models.CharField(max_length=64)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedBy', models.CharField(max_length=64)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]