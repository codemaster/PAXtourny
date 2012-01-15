from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tournament.views',
    # Tournaments
    url(r'^$', 'index'),
    url(r'^tournament/(?P<tournament_id>\d+)$', 'tournament'),
    url(r'^players/$', 'players'),
    url(r'^player/(?P<name>\w+)/$', 'player'),
    url(r'^teams/$', 'teams'),
    url(r'^team/(?P<name>\w+)/$', 'team'),
    url(r'^match/(?P<match_id>\d+)/$', 'match'),
    url(r'^entry/$', 'entry'),
)
