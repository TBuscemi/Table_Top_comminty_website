from django.urls import path
from chat import views

urlpatterns = [
    path('allcharacter_cards/', views.get_all_chat),
    path('postcharacter_cards', views.post_chat),
    path('getcharacter_cards/ ', views.get_chat),
    path('deletecharacter_cards', views.delete),
]