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
    
    def __unicode__(self):
        return self.name
    
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, verbose_name="The tournament that this match belongs to")
    parent = models.ForeignKey("Match", verbose_name="The optional parent match", blank=True, null=True)
    teams = models.ManyToManyField(Team, verbose_name="The teams that are in this match")
    
    def __unicode__(self):
        return " vs ".join([team.name for team in self.teams.all()])