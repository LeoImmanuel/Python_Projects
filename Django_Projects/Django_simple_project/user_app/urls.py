from django.urls import path
from user_app import views

urlpatterns = [
    path('',views.user_page,name="user page")
]