
from django import template
from django.utils.http import urlencode


from goods1.models import categories


register =template.Library()


@register.simple_tag()
def tag_categories():
    return  categories.objects.all()




@register.simple_tag(takes_context=True)
def all_get_page(context, **kwargs):
    query_search = context['request'].GET.dict() 
    query_search.update(kwargs)
    return urlencode(query_search)