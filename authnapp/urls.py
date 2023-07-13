from django.urls import path

import authnapp.views as authnapp

app_name = "users"

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
    path("register/", authnapp.register, name="register"),
    path("edit/", authnapp.edit, name="edit"),
    path('profile/<int:pk>/', authnapp.UserDetailView.as_view(), name='profile'),
]