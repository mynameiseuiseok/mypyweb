from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg  # 원래 값 - 매개 값 -> | sub:arg