from django.urls import path
from friends_list import views

urlpatterns = [
    path('allfriends_list/', views.get_all_friends_list),
    path('postfriends_list', views.post_friends_list),
    path('getfriends_list/ ', views.get_friends_list),
    path('deletefriends_list', views.delete),  
]