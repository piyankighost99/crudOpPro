from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.student_form), #localhost:p/student/list
    path('list/', views.student_list),
]