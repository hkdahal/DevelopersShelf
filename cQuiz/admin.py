from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0
    # if len(Choice.objects.all()) < 4:
    #     extra = 4 - len(model.objects.all())


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('id', 'question_text', 'pub_date')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'c_id', 'choice_text', 'correct')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
