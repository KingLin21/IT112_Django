from django.contrib import admin
from games.models import Game

class GameAdmin(admin.ModelAdmin):
  list_display = ('name', 'genre')
  list_filter = ('genre', 'creator')
  search_fields = ('name', 'creator')
  
  
admin.site.register(Game, GameAdmin)