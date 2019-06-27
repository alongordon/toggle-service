from django import template

from inventit.models import CountLines

register = template.Library()


@register.simple_tag
def summary_colour(line_item):
    if line_item.count_summary == line_item.count_theoretical:
        return "bg-success"

    if line_item.count_summary < line_item.count_theoretical:
        return "bg-danger"

    return "bg-warning"


@register.simple_tag
def get_line_items(item_code):
    return CountLines.objects.filter(inventory__item_code=item_code)
