from django import template

register = template.Library()

@register.filter(name='ipdb')
def ipdb(element):
    import ipdb; ipdb.set_trace()
    return element