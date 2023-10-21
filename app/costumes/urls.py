from django.urls import path
from costumes import views

urlpatterns = [
    path('costumes/', views.CostumeList.as_view()),
    path('costumes/<int:pk>/', views.CostumeDetail.as_view())
]