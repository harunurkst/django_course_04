from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<int:roll>', student_detail, name='student-detail'),
    path('filter/gender/<gender>', student_filter, name='student-filter'),
    path('result', get_result, name='get-result'),
    path('create', create_student, name='create-student'),
]