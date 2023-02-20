from django.shortcuts import render
from .models import Game

def games(request):
  games = Game.objects.all()
  return render(request, 'game.html', {'games':games})

def info(request, game_id):
  game = Game.objects.get(pk=game_id)
  return render(request, 'info.html', {'game':game})