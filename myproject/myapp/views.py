from django.shortcuts import render
from .models import Module4
from django.db import models

def display_grades(request):
    grades = Module4.objects.all()
    grades_count = grades.count()
    min_grade = grades.aggregate(min_grade=models.Min('grade'))['min_grade']
    max_grade = grades.aggregate(max_grade=models.Max('grade'))['max_grade']
    avg_grade = grades.aggregate(avg_grade=models.Avg('grade'))['avg_grade']

    context = {
        'grades': grades,
        'grades_count': grades_count,
        'min': min_grade,
        'max': max_grade,
        'avg': round(avg_grade),
    }

    return render(request, 'grades.html', context)
