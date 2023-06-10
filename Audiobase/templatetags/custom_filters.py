from django import template

register = template.Library()


@register.filter(name='convert_to_path')
def convert_to_path(value):
    return value.replace(" ", "").lower()
