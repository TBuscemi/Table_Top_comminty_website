from django.urls import path
from character_cards import views

urlpatterns = [
    path('', views.CharacterCardsList.as_view())
]
