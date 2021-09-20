from django.urls import path
from character_cards import views

urlpatterns = [
    path('character_cards/', views.Cards.as_view()), 
    path('character_cards/<int:pk>/ ', views.Cards_By_User.as_view()),
   
]
