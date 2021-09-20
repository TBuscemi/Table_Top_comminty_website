from django.urls import path
from chat import views

urlpatterns = [
    path('postcharacter_cards', views.Cards_By_User.as_view()),
]