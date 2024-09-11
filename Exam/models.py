from django.db import models

# Create your models here.

class Courses(models.Model): 
    name = models.CharField(max_length=30)
    added_date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=300, null=True)

    class Meta: 
        verbose_name_plural = 'Courses'

    def __str__(self): 
        return self.name
    
    

class Questions(models.Model): 
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    question = models.CharField(null=False, max_length=150)

    created_date = models.DateTimeField(auto_now_add=True)


    class Meta: 
        verbose_name_plural = 'Questions'



    def __str__(self): 
        return self.question

class Answer(models.Model): 
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='questions')
    answer_text = models.CharField(max_length=250, null=True)
    is_correct = models.BooleanField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)



    def __str__(self): 
        return self.question.question

class Result(models.Model): 
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answers')
    total = models.IntegerField()

    result_date = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    def __str__(self): 
        return self.answer
    
