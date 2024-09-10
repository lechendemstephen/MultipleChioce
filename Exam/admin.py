from django.contrib import admin
from .models import Questions, Courses, Answer, Result
# Register your models here.

# admin management
class CourseAdmin(admin.ModelAdmin): 
    list_display = ('name', 'added_date')

class QuestionAdmin(admin.ModelAdmin): 
    list_display = ('course', 'question', 'created_date')

class AnswerAdmin(admin.ModelAdmin): 
    list_display = ('question', 'is_correct', 'answer_text', 'created_date')

class ResultAdmin(admin.ModelAdmin): 
    list_display = ('question', 'answer', 'total')




admin.site.register(Courses, CourseAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)