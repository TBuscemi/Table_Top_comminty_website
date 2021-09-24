from django.urls import path
from account import views

urlpatterns = [
    path('findall/', views.Accounts_Get.as_view()),
    path('user/<int:uid>/', views.Account_By_User.as_view()),
    path('<int:pk>/ ', views.Account_Query.as_view()),
    path('search/',views.Account_Search.as_view())
]
