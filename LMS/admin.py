from django.contrib import admin
from .models import Gameweek, Choice, Team

# Register your models here.
class GameweekAdmin(admin.ModelAdmin):
        list_display = ('home_team', 'score', 'away_team')

class ChoicesAdmin(admin.ModelAdmin):
        list_display = ('user_id', 'gameweek_id')

class TeamsAdmin(admin.ModelAdmin):
        list_display = ('short_name', 'long_name')


admin.site.register(Gameweek, GameweekAdmin)
admin.site.register(Choice, ChoicesAdmin)
admin.site.register(Team, TeamsAdmin)