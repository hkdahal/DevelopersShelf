from django.shortcuts import render
from .models import Question, Choice


def index(request):
    context = {'mo_it': 'cQuiz', 'my_pages': ['Do 1', 'Do 2', 'Do 3', 'Do 4']}
    return render(request, 'cQuiz/base.html', context=context)


def qa(request):
    questions = Question.objects.all()
    context = {'mo_it': 'cQuiz', 'my_pages': ['Do 1', 'Do 2', 'Do 3', 'Do 4'], 'questions': questions}
    return render(request, 'cQuiz/tukra.html', context=context)
