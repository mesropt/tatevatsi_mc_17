from django.db import models
from helpers.choices import GenderChoices
from helpers.file_storage import doctor_image_storage
from examinations.models import (Examination, MagneticResonanceImagingThreeTesla,
                                  MagneticResonanceImagingOneFiveTesla,
                                  ComputedTomography, XRay,
                                 Mammography, Ultrasound)

class Doctor(models.Model):
    # Examinations:
    magnetic_resonance_imaging_1_5t = models.ManyToManyField(MagneticResonanceImagingOneFiveTesla, related_name='magnetic_resonance_imaging_1_5t', blank=True, null=True)
    magnetic_resonance_imaging_3t = models.ManyToManyField(MagneticResonanceImagingThreeTesla, related_name='magnetic_resonance_imaging_3t', blank=True, null=True)
    computed_tomography = models.ManyToManyField(ComputedTomography, related_name='computed_tomography', blank=True, null=True)
    xray = models.ManyToManyField(XRay, related_name='xray', blank=True, null=True)
    mammography = models.ManyToManyField(Mammography, related_name='mammography', blank=True, null=True)
    ultrasound = models.ManyToManyField(Ultrasound, related_name='ultrasound', blank=True, null=True)
    # Other:
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255, default='')
    seniority = models.IntegerField(null=True, blank=True, help_text='(years)')
    scientific_degree = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GenderChoices.choices, null=True, blank=True)
    image = models.ImageField(upload_to=doctor_image_storage, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"