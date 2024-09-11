from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Answer, Courses
from django.contrib import messages
# Create your views here.

def home(request): 
    courses = Courses.objects.all()

    context = {
        "courses": courses
    }

    return render(request, 'Exams/pages/home.html', context)

def exam_detail(request, exam_name):
    questions = Questions.objects.filter(course__slug = exam_name)
    
    context = {
        "questions": questions,
      
    }

    return render (request, 'Exams/pages/exam_detail.html', context)

def take_quiz(request, quiz_id): 
    answers = Answer.objects.filter(id=quiz_id)
    score = 0
    wrong = 0
    if request.method == "POST": 
            user_answer = request.POST.get('question_{questions.id}')
            for answer in answers: 
                if answer.is_correct == user_answer: 
                    score +=1 
                    messages.success(request, f'you got: {score} correct')
                    return render(request, 'Exams/pages/exam_detail.html', {
                         "score": score 
                    })  
                wrong += 1    
                messages.error(request, f'you got: {wrong}')
                return render(request, 'Exams/pages/exam_detail.html', {
                         "wrong": wrong
                    })    

