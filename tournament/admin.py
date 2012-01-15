from models import Tournament, Player, Match, Team
from django.contrib import admin
import random

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
            
class TournamentAdmin(admin.ModelAdmin):
    actions = ['start_tournament']
    
    def start_tournament(self, request, queryset):
        # For each tournament that we are starting...
        for tournament in queryset:
            # Grab all of the teams that are in a specific tournament
            teams_q = Team.objects.filter(tournaments__id=tournament.id)
            teams = []
            for tq in teams_q:
                teams.append(tq)
            # Randomize the teams!
            random.shuffle(teams)
            round_num = 1
            
            # Create initial matches
            team_offset = 0
            while (len(teams) - team_offset) > 0:
                # If we have enough teams for a match...
                if (len(teams) - team_offset) >= tournament.teams_per_match:
                    # Create a match
                    match = Match()
                    match.round = round_num
                    match.tournament = tournament
                    # Sync back to the DB before adding teams
                    match.save()
                    match.teams
                    for _ in xrange(tournament.teams_per_match):
                    #while len(match.teams) < tournament.teams_per_match:
                        match.teams.add(teams[team_offset])
                        team_offset += 1
                    match.save()
                else:
                    # Since we have teams left, but not enough for a match
                    # We create dud matches with seed teams
                    match = Match()
                    match.round = round_num
                    match.tournament = tournament
                    match.save()
                    if teams[team_offset]:
                        match.teams.add(teams[team_offset])
                        match.teams.winner = teams[team_offset]
                    team_offset += 1
                    
            # Create each round's tournaments
            done = False
            while not done:
                matches = Match.objects.filter(round_num=round_num, tournament=tournament.id)
                if len(matches) > 0:
                    round_num += 1
                    new_matches = (len(matches) / tournament.teams_per_match)
                    new_seeds = (len(matches) % tournament.teams_per_match)
                    if new_matches == 1 and new_seeds == 0:
                        done = True
                    old_matches = []
                    for match in matches:
                        old_matches.append(match)
                    for _ in xrange(new_matches):
                        new_match = Match()
                        new_match.round = round_num
                        new_match.tournament = tournament
                        new_match.save()
                        for _ in xrange(tournament.teams_per_match):
                            t_match = old_matches.pop()
                            t_match.child = new_match
                            t_match.save()
                    while new_seeds >= tournament.teams_per_match:
                        new_match = Match()
                        new_match.round = round_num
                        new_match.tournament = tournament
                        new_match.save()
                        for _ in xrange(tournament.teams_per_match):
                            t_match = old_matches.pop()
                            t_match.child = new_match
                            t_match.save()
                        new_seeds -= tournament.teams_per_match
                    for _ in xrange(new_seeds):
                        new_match = Match()
                        new_match.round = round_num
                        new_match.tournament = tournament
                        new_match.save()
                        t_match = old_matches.pop()
                        t_match.child = new_match
                        new_match.save()
                        t_match.save()
                else:
                    done = True
            
    start_tournament.short_description = 'Starts the tournaments by making associated matches'
            
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match)
admin.site.register(Team)