
from django import template
from Main.forms import SubscriberForm
register = template.Library()


@register.simple_tag
def get_subscriber_form():
    return SubscriberForm