# Generated by Django 4.1.2 on 2022-11-04 18:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Group ID ')),
                ('uuid_group', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Group Name')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Room ID')),
                ('room_name', models.CharField(max_length=250, verbose_name='Room Name')),
                ('password', models.CharField(blank=True, max_length=250, verbose_name='Password')),
                ('is_research', models.BooleanField(default=True, verbose_name='Research')),
            ],
        ),
        migrations.CreateModel(
            name='GameSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=250, verbose_name='Host')),
                ('arithmetic', models.CharField(max_length=250, verbose_name='Arithmetic')),
                ('difficulty', models.CharField(max_length=250, verbose_name='Difficulty')),
                ('speed', models.CharField(max_length=250, verbose_name='Speed')),
                ('lvl', models.CharField(max_length=250, verbose_name='lvl')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multiPlayer.room', verbose_name='room')),
            ],
        ),
    ]