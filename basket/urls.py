from django.urls import path
from users import views

app_name = 'basket'

urlpatterns = [
    path('register/', views.register_user, name='register'),
]