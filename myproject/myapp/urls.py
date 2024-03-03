from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.display_grades, name='display_grades'),
]