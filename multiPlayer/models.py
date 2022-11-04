from django.db import models
from datetime import datetime, date
import uuid

# Create your models here.

class Group(models.Model):
  id = models.AutoField(primary_key=True, verbose_name='Group ID ')
  uuid_group = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  name = models.CharField(max_length=250, verbose_name='Group Name', unique=True)

  def __str__(self):
    return self.name

class Room(models.Model):
  id =  models.AutoField(primary_key=True, verbose_name='Room ID')
  room_name = models.CharField(max_length=250, verbose_name='Room Name')
  password = models.CharField(max_length=250, verbose_name='Password', blank=True)
  is_research = models.BooleanField(default=True, verbose_name="Research")

  def __str__(self):
    return self.room_name

class GameSetting(models.Model):
  room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="room")
  host = models.CharField(max_length=250, verbose_name='Host')
  arithmetic = models.CharField(max_length=250, verbose_name='Arithmetic')
  difficulty = models.CharField(max_length=250, verbose_name='Difficulty')
  speed = models.CharField(max_length=250, verbose_name='Speed')
  lvl = models.CharField(max_length=250, verbose_name='lvl')

  def __str__(self):
    return  self.room

