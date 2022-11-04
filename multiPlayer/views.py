from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Assessment.models import * 
from multiPlayer.models import * 
import json

def multiPlayerMenu(request):
  output = {"header_name": "Multiplayer Menu"}
  return render(request, "multiPlayer/menu.html", output)

def hostGame(request):
  return render(request, "multiPlayer/hostGame.html")

def lobby(request, uuid):
  user_uuid = uuid
  request.session['uuid'] = user_uuid
  user = Player.objects.filter(uuid=uuid).first()
  user_name = user.username
  out = {
      "user_1":user_name
  }
  return render(request, "multiPlayer/lobby.html",out)

def lobbyAjax(request):
  if request.method == 'POST':
    studentUUID = request.POST['studentUUID']
    user = Player.objects.filter(uuid=studentUUID).first()

    if user.group == None:
      message = "No Group"
    else:
      message = user.group

    return HttpResponse(message)

def multiPlayerSettings(request, room_name, uuid):
  game_setting_room, created = Room.objects.get_or_create(room_name=room_name)
  player = Player.objects.get(uuid=uuid)
  out = {
    "room": game_setting_room,
    'player': player
  }
  return render(request, "multiPlayer/multiPlayerSettings.html", out)
    
# def multiPlayerGameplay(request, room_name):
#   game_setting_room, created = Room.objects.get_or_create(room_name=room_name)
#   out = {
#     "room": game_setting_room
#   }
#   return render(request, "multiPlayer/multiPlayerGameplay.html", out)

def multiPlayerRooms(request, uuid):
  
  player = Player.objects.get(uuid=uuid)

  rooms = Room.objects.all()
  out = {
    'uuid': uuid,
    'player': player,
    'rooms': rooms
  }
  return render(request, "multiPlayer/room.html", out)