from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from examinations.models import (Examination, MagneticResonanceImaging,
                                 ComputedTomography, XRay,
                                 Mammography, Ultrasound)
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView


class ExaminationDetailView(DetailView):
    model = Examination
    template_name = 'examination/detail.html'

class ExaminationDetailView(DetailView):
    model = Examination
    template_name = 'examination/detail.html'


class ExaminationAddlView(DetailView):
    model = Examination
    template_name = 'examination/detail.html'


class ExaminationUpdateView(DetailView):
    model = Examination
    template_name = 'examination/detail.html'

class ExaminationDeleteView(DetailView):
    model = Examination
    template_name = 'examination/detail.html'

class ExaminationListView(DetailView):
    model = Examination
    template_name = 'examination/detail.html'
