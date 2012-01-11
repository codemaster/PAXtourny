from tournament.models import Tournament, Player, Team, Match
from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    all_tournaments = Tournament.objects.all().order_by('name')
    t = loader.get_template('main.html')
    c = Context({
        'tournaments' : all_tournaments
    })
    return HttpResponse(t.render(c))
    #output = '<ul>' + ''.join(['<li>' + t.name + '</li>' for t in all_tournaments]) + '</ul>'
    #return HttpResponse(output)

def tournament(request, tournament_id):
    return HttpResponse("This will return all of the information about the " + tournament_id + " tournament")

def players(request):
    return HttpResponse("This will list all the players in the tournaments")

def player(request, name):
    return HttpResponse("This will list all of the information about the player " + name)

def teams(request):
    return HttpResponse("This will list all of the teams in the tournaments")

def team(request, name):
    return HttpResponse("This will list the information about the team " + name)

def match(request, match_id):
    return HttpResponse("This will list the information about the match #" + match_id)

def entry(request):
    return HttpResponse("This will provide forms for entering a new player & team")