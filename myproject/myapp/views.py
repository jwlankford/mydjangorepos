from django.shortcuts import render
from .models import Module4

def display_grades(request):
    grades = [ 34,45,67,89,90]
    grades2 = Module4.objects.values_list('grade', flat=True)
    gcount = grades2
    print(grades2)
    min_grade = min(grades)
    max_grade = max(grades)
    avg_grade = sum(grades) / len(grades)
    return render(request, 'grades.html', {'min': min_grade, 'max': max_grade, 'avg': avg_grade, 'grades': grades2, 'gradecount': gcount})

# def display_grades(request):
#     return render(request, 'grades.html', {'grades': Module4.objects.all()})