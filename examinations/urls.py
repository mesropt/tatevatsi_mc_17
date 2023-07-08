from django.urls import path
from examinations import views

app_name = 'examinations'
urlpatterns = [
    path('', views.ExaminationListView.as_view(), name='list'),
    path('details/<int:pk>/', views.ExaminationDetailView.as_view(), name='detail'),
    path('add/', views.ExaminationAddlView.as_view(), name='add'),
    path('update/<int:pk>/', views.ExaminationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ExaminationDeleteView.as_view(), name='delete'),
]