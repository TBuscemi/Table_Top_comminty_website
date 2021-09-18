from django.urls import path
from character_cards import views

urlpatterns = [
    path('allcharacter_cards/', views.get_all_character_cards),
    path('postcharacter_cards', views.post_character_cards),
    path('getcharacter_cards/ ', views.get_character_cards),
    path('deletecharacter_cards', views.delete),
]
