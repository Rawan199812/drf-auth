from django.urls import path
from .views import StudentsList, StudentsDetail

urlpatterns = [
    path('', StudentsList.as_view(), name='students_list'),
    path('<int:pk>/', StudentsDetail.as_view(), name='students_detail'),
]