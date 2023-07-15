from django.views.generic import DetailView, TemplateView

from examinations.models import (
    ComputedTomography,
    Examination,
    MagneticResonanceImagingOneFiveTesla,
    MagneticResonanceImagingThreeTesla,
    Mammography,
    Ultrasound,
    XRay,
)


class ExaminationsListView(TemplateView):
    template_name = "examinations/examinations_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        examination_lists = {
            "magnetic_resonance_imaging_three_tesla": MagneticResonanceImagingThreeTesla.objects.all(),
            "magnetic_resonance_imaging_one_five_tesla": MagneticResonanceImagingOneFiveTesla.objects.all(),
            "computed_tomography": ComputedTomography.objects.all(),
            "xray": XRay.objects.all(),
            "mammography": Mammography.objects.all(),
            "ultrasound": Ultrasound.objects.all(),
        }
        context["examination_lists"] = examination_lists

        return context


class ExaminationsDetailView(DetailView):
    template_name = "examinations/examination_detail.html"
    context_object_name = "examination"

    def get_model(self):
        examination_type = self.kwargs.get("examination_type")

        if examination_type == "magnetic_resonance_imaging_three_tesla":
            return MagneticResonanceImagingThreeTesla
        elif examination_type == "magnetic_resonance_imaging_one_five_tesla":
            return MagneticResonanceImagingOneFiveTesla
        elif examination_type == "computed_tomography":
            return ComputedTomography
        elif examination_type == "xray":
            return XRay
        elif examination_type == "mammography":
            return Mammography
        elif examination_type == "ultrasound":
            return Ultrasound

    def get_queryset(self):
        model = self.get_model()
        queryset = model._default_manager.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        examination_type = self.kwargs.get("examination_type")

        examination_list = self.get_queryset()
        context["examination_list"] = examination_list

        return context


# class ExaminationsIndexView(DetailView):
#     template_name = 'home/index.html'
#     context_object_name = 'examination'
#
#     def get_model(self):
#         examination_type = self.kwargs.get('examination_type')
#
#         if examination_type == 'magnetic_resonance_imaging_three_tesla':
#             return MagneticResonanceImagingThreeTesla
#         elif examination_type == 'magnetic_resonance_imaging_one_five_tesla':
#             return MagneticResonanceImagingOneFiveTesla
#         elif examination_type == 'computed_tomography':
#             return ComputedTomography
#         elif examination_type == 'xray':
#             return XRay
#         elif examination_type == 'mammography':
#             return Mammography
#         elif examination_type == 'ultrasound':
#             return Ultrasound
#
#     def get_queryset(self):
#         model = self.get_model()
#         queryset = model._default_manager.all()
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         examination_type = self.kwargs.get('examination_type')
#
#         examination_list = self.get_queryset()
#         context['examination_list'] = examination_list
#
#         return context
