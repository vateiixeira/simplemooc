from django import template

register = template.Library()

from simplemooc.courses.models import Enrollment

@register.simple_tag
def load_my_course(user):
    return Enrollment.objects.filter(user=user)