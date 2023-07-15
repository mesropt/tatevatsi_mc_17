from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView

from doctors.models import Doctor


class DoctorsListView(TemplateView):
    template_name = "doctors/doctors_list.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = Doctor.objects.all().order_by("pk")

        # Search doctors
        search_query = self.request.GET.get("search_query")
        if search_query:
            doctors = doctors.filter(
                Q(first_name__icontains=search_query)
                | Q(last_name__icontains=search_query)
            )

        paginator = Paginator(doctors, self.paginate_by)
        page_number = self.request.GET.get("page")
        doctors = paginator.get_page(page_number)
        context["doctors_list"] = doctors
        return context


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "doctors/doctor_detail.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(Doctor, pk=pk)
