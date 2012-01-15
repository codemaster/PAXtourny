from models import Tournament, Player, Match, Team
from django.contrib import admin

class PlayerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            team = Team()
            team.name = obj.handle + " (Team)"
            team.save()
            obj.save()
            team.members.add(obj)
            team.save()
        else:
            obj.save()
            
admin.site.register(Tournament)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match)
admin.site.register(Team)