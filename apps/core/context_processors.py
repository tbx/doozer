from django.core.urlresolvers import reverse
from django.conf import settings

def nav(request):
    menu = {
        'menu' : [
            ('Home', 'home'),
            ('Gallery', 'games.view_list'),
            ('Categories', 'categories'),
            ('Judges', 'judges'),
            ('Prizes', 'prizes'),
            ('Parties', 'parties'),
        ],
        'location' : request.path,
    }
    if not settings.ALLOW_GALLERY:
        menu['menu'].pop(1)
    return menu

def global_settings(request):
    return {'settings': settings}