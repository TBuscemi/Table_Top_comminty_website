from django.urls import path
from videos import views

urlpatterns = [
    path('settingupvideos/', views.Videos_tutorials.as_view()),
    path('settingupvideos/<int:pk>/', views.Videos_tutorials.as_view()),
    
]