from django.conf import settings
from django.http import Http404

from django import template

from core.template import render


def party(request, party_name):
    """Show a static page for a party"""
    try:
        return render(request, 'static/parties/%s.html' % party_name)
    except template.TemplateDoesNotExist:
        raise Http404

