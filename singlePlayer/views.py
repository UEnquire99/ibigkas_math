# Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


from django.views.decorators.csrf import csrf_exempt


# External Imports 
import json 

# Internal Imports
from . import utility as utils 
from . import filter_question_data as filter_qa
from Assessment.models import * 
from singlePlayer.models import *
from .forms import SettingsForm

def singlePlayerMenu(request, uuid):
  user_uuid = uuid
  request.session['uuid'] = user_uuid
  Player.objects.filter(uuid=uuid).update(player_mode="SinglePlayer")
  return render(request, "singlePlayer/singlePlayerMenu.html")

def singlePlayerSettings(request, uuid):
  user_uuid = uuid
  request.session['uuid'] = user_uuid
  return render(request, "singlePlayer/gameSettings.html")


def singlePlayerSettingsAjax(request):
  if request.method == 'POST':
    arithmeticResults = request.POST['arithmeticResults']
    difficultyResults = request.POST['difficultyResults']
    year_level = request.POST['year_level']
    speed = request.POST['speed']
    studentUUID = request.POST['studentUUID']

    def newFormat(s):
      s = s.translate({ord('['): None})
      s = s.translate({ord(']'): None})
      s = s.translate({ord('"'): None})
      return s
    
    arithmeticResults = newFormat(arithmeticResults)
    difficultyResults = newFormat(difficultyResults)
    
    if speed == "medium-two":
      speed = "medium"

    settings = {
        'arithmetic' : arithmeticResults,
        'lvl' : year_level,
        'speed' : speed,
        'difficulty' : difficultyResults
    }

    player_name = Player.objects.get(uuid=studentUUID)
      
    create_setting = GameSetting(
        player = player_name,
        arithmetic = settings['arithmetic'],
        difficulty = settings['difficulty'],
        speed = settings['speed'],
        lvl = settings['lvl']
    )
    create_setting.save()
    pk = create_setting.setting_id
    return HttpResponse(pk)

@csrf_exempt
def userGameResults(request):
  if request.method == 'POST':
    game_history = request.POST['game_history']
    correct_answer = request.POST['correct_answer']
    wrong_answer = request.POST['wrong_answer']
    total_questions = request.POST['total_questions']
    speed = request.POST['speed']
    studentUUID = request.POST['studentUUID']
    Player.objects.filter(uuid=studentUUID).update(game_answer_history=game_history, total_questions=total_questions,
    correct_answers = correct_answer, wrong_answers = wrong_answer, speed = speed
    )
    return HttpResponse('Data save!')


    
def singlePlayerHowToPlay(request):
  return render(request, "singlePlayer/howToPlay.html")




def singlePlayerGamePlay(request, pk): 
  setting_entry = GameSetting.objects.get(setting_id = pk)
  settings = utils.user_input(setting_entry)

  data = filter_qa.filter_question_dataset(settings)
  game_round_state = utils.init_game_round_variables()

  out = {
    "settings": settings,  
    "json_settings": json.dumps(settings),
    "json_game_round_state": json.dumps(game_round_state),
    "json_data" : json.dumps(data) 
  }
  return render(request, "singlePlayer/gameplay.html", out)
