# from email import message
import json 
from channels.generic.websocket import WebsocketConsumer 
from asgiref.sync import async_to_sync
from multiPlayer.models import * 

class MultiplayerSettings(WebsocketConsumer):

  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)
    self.room_name = None
    self.room_group_name = None
    self.room = None


  def connect(self):
    print("TESTING: ", self.scope)

    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = f'chat_{self.room_name}'
    self.room = Room.objects.get(room_name=self.room_name)

    # connection has to be accepted
    self.accept()

    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )

  
  def disconnect(self, close_code):
    async_to_sync(self.channel_layer.group_discard)(
      self.room_group_name,
      self.channel_name,
    )
    
  
  def receive(self, text_data=None, bytes_data=None):
    text_data_json = json.loads(text_data)
    player_name = text_data_json['player_name']

    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'player_name_method',
        'message': player_name
      }
    )
  
  def player_name_method(self, event):
    self.send(text_data=json.dumps(event))