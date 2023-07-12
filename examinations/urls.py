from django.urls import path
from examinations import views

app_name = 'examinations'

urlpatterns = [
    path('list/', views.ExaminationsListView.as_view(), name='list'),
    path('detail/<str:examination_type>/<int:pk>/', views.ExaminationsDetailView.as_view(), name='detail'),
]
