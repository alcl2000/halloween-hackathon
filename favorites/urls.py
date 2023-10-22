from django.urls import path
from . import views

urlpatterns = [
    path('favorites/', views.FavoriteList.as_view()),
    path('favorite-costumes/<int:pk>/', views.FavoriteDetail.as_view(), name='favorite-costume-detail'),
    path('costume/<int:costume_id>/save/', views.FavoriteCostumePost.as_view(), name='favorite-costume-post'),

]