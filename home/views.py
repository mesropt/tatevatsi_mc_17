from django.shortcuts import render
from examinations.models import MagneticResonanceImagingThreeTesla
# def home(request):
#     context = {
#         'model_name': MagneticResonanceImagingThreeTesla.html_name
#     }
#     return render(request, 'home/index.html', context)

def home(request):
    mri_3t = MagneticResonanceImagingThreeTesla.objects.first()
    context = {
        'mri_3t': mri_3t,
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')