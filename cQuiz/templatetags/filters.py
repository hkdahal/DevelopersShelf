from django import template
from cQuiz.models import Choice

register = template.Library()


@register.filter
def get_choices(question):
    return Choice.objects.filter(question=question)[0].choice_text
