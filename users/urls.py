from django.urls import path
from django.contrib.auth.views import LoginView
from users.views import UserTemplateView, EmailFormView, RegistrationView, ActivateAccountView, UserDetailView
from users import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('user-template/', views.UserTemplateView.as_view(), name='user_template'),
    path('email-template/', views.EmailFormView.as_view(), name='email_form'),
    path('register/', views.RegistrationView.as_view(), name='registration'),
    path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/<int:pk>/', views.UserUpdateView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

