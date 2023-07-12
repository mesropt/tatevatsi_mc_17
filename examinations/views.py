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

        examinations_three_tesla = MagneticResonanceImagingThreeTesla.objects.all()
        context['examinations_three_tesla'] = examinations_three_tesla

        examinations_one_five_tesla = MagneticResonanceImagingOneFiveTesla.objects.all()
        context['examinations_one_five_tesla'] = examinations_one_five_tesla

        examinations_computed_tomography = ComputedTomography.objects.all()
        context['examinations_computed_tomography'] = examinations_computed_tomography

        examinations_xray = XRay.objects.all()
        context['examinations_xray'] = examinations_xray

        examinations_mammography = Mammography.objects.all()
        context['examinations_mammography'] = examinations_mammography

        examinations_ultrasound = Ultrasound.objects.all()
        context['examinations_ultrasound'] = examinations_ultrasound

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
