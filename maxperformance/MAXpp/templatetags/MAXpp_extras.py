from django import template

register = template.Library()


@register.filter
def return_item(l, i):
    return l[i]
