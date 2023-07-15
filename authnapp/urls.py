from django.urls import path

import authnapp.views as authnapp

app_name = "users"

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
    path("register/", authnapp.register, name="register"),
    path("edit/", authnapp.edit, name="edit"),
    path('profile/<int:pk>/', authnapp.UserDetailView.as_view(), name='profile'),
    path('profile/delete/<int:pk>/', authnapp.delete_user, name='user_delete'),
    path('profile/update/<int:pk>/', authnapp.UserUpdateView.as_view(),
         name='user_update'),

]