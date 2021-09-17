from django.urls import path
from account import views

urlpatterns = [
    path('all/', views.get_all_accounts),
    path(' ', views.User_post)
]
