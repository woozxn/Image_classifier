from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.gallery, name='gallery'),
    path('all/',views.all_photo,name='all_photo'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('photo/<str:pk>/delete/', views.photo_delete, name='photo_delete'),
    path('add/', views.addPhoto, name='add'),
]