from atexit import register
from django import template
register=template.Library()

@register.filter('quots')
def quots(value):
    value='"'+value+'"'
    return value