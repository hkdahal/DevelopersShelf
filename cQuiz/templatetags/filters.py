from django import template
from cQuiz.models import Choice
from random import shuffle

register = template.Library()


@register.filter
def get_choices(question):
    return Choice.objects.filter(question=question)[0].choice_text


@register.filter
def decrement_me(num):
    return num-1


@register.filter
def randomize_list(choices):
    lst = [i for i in choices]
    shuffle(lst)
    return lst
