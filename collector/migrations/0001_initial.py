# Generated by Django 3.1.7 on 2021-04-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('data', models.JSONField()),
            ],
        ),
    ]