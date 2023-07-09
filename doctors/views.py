from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator
from doctors.models import Doctor

class DoctorsListView(TemplateView):
    template_name = 'doctors/doctors_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = Doctor.objects.all().order_by('-pk')
        paginator = Paginator(doctors, self.paginate_by)
        page_number = self.request.GET.get("page")
        doctors = paginator.get_page(page_number)
        context['doctors_list'] = doctors
        return context

# def doctors_list(request):
#     doctors = Doctor.objects.all().order_by('-pk')
#     paginator = Paginator(doctors, 4)  # Show 25 contacts per page.
#     page_number = request.GET.get("page")
#     doctors = paginator.get_page(page_number)
#     return render(request, 'doctors/doctors_list.html', {'doctors_list': doctors})

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