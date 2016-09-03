from django.shortcuts import render


def index(request):
    context = {'mo_it': 'cQuiz', 'my_pages': ['Do 1', 'Do 2', 'Do 3', 'Do 4']}
    return render(request, 'cQuiz/index.html', context=context)
