from django.urls import path
from account import views

urlpatterns = [
    path('allaccount/', views.get_all_accounts),
    path('postaccount', views.post_user),
    path('getaccount/ ', views.get_account),
    path('deleteaccount', views.delete),
    
]
