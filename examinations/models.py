from django.db import models
from abc import abstractmethod
from helpers.file_storage import examination_images_storage

# ABSTRACT CLASS:
class Examination(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    html_name = None
    description = models.TextField(null=True, blank=True)
    doctor = models.ManyToManyField('Doctor', related_name='examinations', null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=examination_images_storage)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=True, blank=True)

    # @abstractmethod
    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


# SUBCLASSES:
class MagneticResonanceImagingThreeTesla(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='magnetic_resonance_imaging_3t', blank=True, null=True)

    class Meta:
        verbose_name = 'Magnetic Resonance Imaging (3 Tesla)'
        verbose_name_plural = 'Magnetic Resonance Imagings (3 Tesla)'

    html_name = 'MRI 3T'

class MagneticResonanceImagingOneFiveTesla(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='magnetic_resonance_imaging_1_5t', blank=True, null=True)

    class Meta:
        verbose_name = 'Magnetic Resonance Imaging (1.5 Tesla)'
        verbose_name_plural = 'Magnetic Resonance Imagings (1.5 Tesla)'

    html_name = 'MRI 1.5T'

class ComputedTomography(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='computed_tomography', blank=True, null=True)

    class Meta:
        verbose_name = 'Computed Tomography'
        verbose_name_plural = 'Computed Tomographies'

    html_name = 'Computed Tomography'

class XRay(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='xray', blank=True, null=True)

    class Meta:
        verbose_name = 'X-Ray'
        verbose_name_plural = 'X-Rays'

    html_name = 'X-Ray'

class Mammography(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='mammography', blank=True, null=True)

    class Meta:
        verbose_name = 'Mammography'
        verbose_name_plural = 'Mammographies'

    html_name = 'Mammography'

class Ultrasound(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='ultrasound', blank=True, null=True)

    class Meta:
        verbose_name = 'Ultrasound'
        verbose_name_plural = 'Ultrasounds'

    html_name = 'Ultrasound'
