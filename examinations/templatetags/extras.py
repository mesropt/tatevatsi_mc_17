# Create a file named 'templatetags/extras.py' in your Django app directory

from django import template

register = template.Library()


@register.filter
def get_class_name(instance):
    return instance.__class__.user_friendly_name


@register.simple_tag
def examination_type_section(examination_type, examinations):
    return ""
