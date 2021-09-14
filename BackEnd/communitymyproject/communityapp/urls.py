from . import views 
from django.urls import path, include

app_name ='communityapp'
urlpatterns = [
    path('',views.index,name=views.index)
]
