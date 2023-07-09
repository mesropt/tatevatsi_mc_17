from django.views.generic import TemplateView, DetailView
from doctors.models import Doctor
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator



# class DoctorDetailView(DetailView):
#     model = Doctor
#     template_name = 'examination/detail.html'
#
#
# class DoctorAddView(DetailView):
#     model = Doctor
#     template_name = 'examination/detail.html'
#
#
# class DoctorUpdateView(DetailView):
#     model = Doctor
#     template_name = 'examination/detail.html'
#
#
# class DoctorDeleteView(DetailView):
#     model = Doctor
#     template_name = 'examination/detail.html'


# class DoctorListView(DetailView):
#     model = Doctor
#     template_name = 'doctors/doctors_list.html'
#


def doctors_list(request):
    doctors = Doctor.objects.all().order_by('-pk')
    paginator = Paginator(doctors, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    doctors = paginator.get_page(page_number)
    return render(request, 'doctors/doctors_list.html', {'doctors_list': doctors})