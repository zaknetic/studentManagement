from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('home/', views.home , name='home'),
    path('home/',views.StudentList.as_view(), name='home'),
    # path('creat/', views.create_student, name='create_student'),
    path('creat/', views.CreatStudent.as_view(), name='create_student'),
    # path('edit/<int:id>/', views.update_student, name='update_student'),
    path('edit/<int:id>/', views.UpdaeStudent.as_view(), name='update_student'),
    # path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('delete/<int:id>/', views.DeleteStudent.as_view(), name='delete_student'),
]
