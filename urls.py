from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from core.views import party

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('registration.urls')),
    (r'^gallery/', include('games.urls')),
    (r'^vote', include('vote.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'static/home.html'}, name='home'),
    url(r'^how$', direct_to_template, {'template': 'static/how.html'}, name='how'),
    url(r'^categories$', direct_to_template, {'template': 'static/categories.html'}, name='categories'),
    url(r'^fineprint$', direct_to_template, {'template': 'static/fineprint.html'}, name='fineprint'),
    url(r'^prizes$', direct_to_template, {'template': 'static/prizes.html'}, name='prizes'),
    url(r'^judges$', direct_to_template, {'template': 'static/judges.html'}, name='judges'),
    url(r'^judging$', direct_to_template, {'template': 'static/judging.html'}, name='judging'),
    url(r'^parties$', direct_to_template, {'template': 'static/parties.html'}, name='parties'),
    url(r'^parties/(?P<party_name>[\w-]+)?', party, name='party'),
)

if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT}),
    )
