from django.db import models

class Tournament(models.Model):
    name = models.CharField("Name of the tournament", max_length=255)
    team_size = models.PositiveSmallIntegerField("Size of the teams for this tournament")
    teams_per_match = models.PositiveSmallIntegerField("Number of teams that will be in each match")
    
    def __unicode__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField("Player's name", max_length=255)
    handle = models.CharField("Player's handle/nickname", max_length=255)
    email = models.EmailField("Player's e-mail address", unique=True)
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.handle)
    
class Team(models.Model):
    name = models.CharField("The name of the teams", max_length=255)
    members = models.ManyToManyField(Player, verbose_name="The players on the team")
    tournaments = models.ManyToManyField(Tournament, verbose_name="The tournaments that this team has signed up for", null=True)
    
    def __unicode__(self):
        return self.name
    
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, verbose_name="The tournament that this match belongs to")
    child = models.ForeignKey("Match", verbose_name="The optional child match", blank=True, null=True)
    teams = models.ManyToManyField(Team, verbose_name="The teams that are in this match")
    winner = models.ForeignKey(Team, verbose_name="The team that won",related_name='wining_team',blank=True,null=True)
    round_num = models.PositiveSmallIntegerField(default=1)
    
    def __unicode__(self):
        return " vs ".join([team.name for team in self.teams.all()])