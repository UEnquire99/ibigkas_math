from django.urls import path
from . import views 

app_name = 'multiPlayer'

urlpatterns = [ 
  path("multiplayer-menu/", views.multiPlayerMenu, name="multiPlayerMenu"),
  path("host-game/", views.hostGame, name="host_game"),
  path("lobby/<uuid>/", views.lobby, name="lobby"),

  # Using Django Channels
  path("multiplayer-rooms/<uuid>/", views.multiPlayerRooms, name="multiPlayerGameplay"),
  path('<str:room_name>/settings/<uuid>/', views.multiPlayerSettings, name='multiplayerSettings'),

  # Ajax
  path("joinRoomAjax/", views.lobbyAjax, name="joinRoomAjax"),
]