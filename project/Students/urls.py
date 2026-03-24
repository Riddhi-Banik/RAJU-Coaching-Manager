from django.urls import path 
from Students import views as S_views

urlpatterns = [
    path('Students/', S_views.student)
]
