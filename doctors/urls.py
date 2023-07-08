from django.urls import path
from doctors import views

app_name = 'doctors'
urlpatterns = [
    path('list', views.DoctorListView.as_view(), name='list'),
    path('details/<int:pk>/', views.DoctorDetailView.as_view(), name='detail'),
    path('add/', views.DoctorAddView.as_view(), name='add'),
    path('update/<int:pk>/', views.DoctorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DoctorDeleteView.as_view(), name='delete'),
]