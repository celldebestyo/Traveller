from django import template
register = template.Library()

@register.filter(name='shortname')
def shortname(name):
    sp = name.split(' ')
    return sp[0][0] + sp[1][0]


