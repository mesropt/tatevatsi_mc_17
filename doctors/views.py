from django.views.generic import TemplateView, DetailView
from doctors.models import Doctor

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'examination/detail.html'


class DoctorAddView(DetailView):
    model = Doctor
    template_name = 'examination/detail.html'


class DoctorUpdateView(DetailView):
    model = Doctor
    template_name = 'examination/detail.html'


class DoctorDeleteView(DetailView):
    model = Doctor
    template_name = 'examination/detail.html'


class DoctorListView(DetailView):
    model = Doctor
    template_name = 'examination/detail.html'