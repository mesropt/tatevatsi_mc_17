from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('profile/', views.home, name='profile'),
    path('contact/', views.home, name='contact')
]

