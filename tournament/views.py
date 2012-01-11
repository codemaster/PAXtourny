from tournament.models import Tournament, Player, Team, Match
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    try:
        tournaments = Tournament.objects.all().order_by('name')
    except Tournament.DoesNotExist:
        raise Http404
    return render_to_response('main.html', {'tournaments' : tournaments})

def tournament(request, tournament_id):
    t = get_object_or_404(Tournament, pk = tournament_id)
    return render_to_response('tournament.html', {'tournament':t})

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