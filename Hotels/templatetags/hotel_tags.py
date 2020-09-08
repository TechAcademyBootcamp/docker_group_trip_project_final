from django import template
register = template.Library()


@register.simple_tag
def get_star_count(star_count):
    star_html = ''
    for i in  range(int(star_count)):
        star_html=star_html+'<span class="fa fa-star checked"> </span>'
    for i in range(int(5-star_count)):
        star_html=star_html+'<span class="fa fa-star"></span>'
    return star_html