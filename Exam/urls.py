from django.urls import path
from . import views

urlpatterns = [
    path("exams/", views.home, name="home"),
    path("exams/<slug:exam_name>/", views.exam_detail, name="exam_detail"),
    path("exams/<int:quiz_id>/", views.take_quiz, name='take_quiz')
    
  
    
]
