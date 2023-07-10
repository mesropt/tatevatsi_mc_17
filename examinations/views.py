from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator
from examinations.models import (Examination, MagneticResonanceImagingThreeTesla,
                                  MagneticResonanceImagingOneFiveTesla,
                                  ComputedTomography, XRay,
                                  Mammography, Ultrasound)


class ExaminationsListView(TemplateView):
    template_name = 'examinations/examinations_list.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        examinations = []
        examinations.extend(MagneticResonanceImagingThreeTesla.objects.all())
        examinations.extend(MagneticResonanceImagingOneFiveTesla.objects.all())
        examinations.extend(ComputedTomography.objects.all())
        examinations.extend(XRay.objects.all())
        examinations.extend(Mammography.objects.all())
        examinations.extend(Ultrasound.objects.all())
        # Add more lines here for other subclasses of Examination

        examinations.sort(key=lambda x: x.pk, reverse=True)

        paginator = Paginator(examinations, self.paginate_by)
        page_number = self.request.GET.get("page")
        examinations = paginator.get_page(page_number)

        context['examinations_list'] = examinations
        return context


class ExaminationsDetailView(DetailView):
    template_name = 'examinations/examination_detail.html'
    context_object_name = 'examination'

    def get_model(self):
        # Determine the appropriate model based on the examination type
        examination_type = self.kwargs.get('examination_type')
        if examination_type == 'magnetic_resonance_imaging_three_tesla':
            return MagneticResonanceImagingThreeTesla
        elif examination_type == 'magnetic_resonance_imaging_one_five_tesla':
            return MagneticResonanceImagingOneFiveTesla
        elif examination_type == 'computed_tomography':
            return ComputedTomography
        elif examination_type == 'xray':
            return XRay
        elif examination_type == 'mammography':
            return Mammography
        elif examination_type == 'ultrasound':
            return Ultrasound
        # Add more conditions for other subclasses of Examination

    def get_queryset(self):
        model = self.get_model()
        queryset = model._default_manager.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examination_type'] = self.kwargs.get('examination_type')
        return context
