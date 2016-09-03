from .models import Question, Choice
from django.utils import timezone
import os


def update():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'q.txt')
    questions = []
    choices = []

    with open(file_path) as a_file:
        q_counter = 0
        c_counter = 0
        current_q = None
        for line in a_file:
            line = line.strip()
            if line.startswith("#"):
                line = line.replace("#", "")
                q_counter += 1
                c_counter = 0
                current_q = Question(question_text=line, pub_date=timezone.now(), q_id=q_counter)
                questions.append(current_q)
            else:
                c_counter += 1
                answer = Choice(choice_text=line, correct=True, question=current_q, c_id=c_counter)
                choices.append(answer)
    return questions, choices


def update_choices():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'q.txt')
    questions = Question.objects.all()
    answers = []
    with open(file_path) as a_file:
        q_counter = 0
        c_counter = 0
        for line in a_file:
            line = line.strip()
            if line.startswith("#"):
                q_counter += 1
                c_counter = 0
            else:
                c_counter += 1
                answer = Choice(choice_text=line, correct=True, question=questions[q_counter-1], c_id=c_counter)
                answers.append(answer)

    return answers


