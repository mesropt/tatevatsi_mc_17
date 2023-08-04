from django.urls import path
from doctors import views

app_name = "doctors"
urlpatterns = [
    path("list", views.DoctorsListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.DoctorDetailView.as_view(), name="detail"),
]
