# Create a file named 'templatetags/extras.py' in your Django app directory

from django import template

register = template.Library()

@register.filter
def get_class_name(instance):
    return instance.__class__.html_name