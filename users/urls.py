from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('profile/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('list-profiles/', views.UserListView.as_view(), name='user_list'),
]