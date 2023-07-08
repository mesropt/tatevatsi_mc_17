from django.db import models
from abc import abstractmethod
from helpers.file_storage import examination_images_storage

# ABSTRACT CLASS:
class Examination(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
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
class MagneticResonanceImaging(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='magnetic_resonance_imaging', blank=True, null=True)

    class Meta:
        verbose_name = 'Magnetic Resonance Imaging'
        verbose_name_plural = 'Magnetic Resonance Imagings'



class ComputedTomography(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='computed_tomography', blank=True, null=True)

    class Meta:
        verbose_name = 'Computed Tomography'
        verbose_name_plural = 'Computed Tomographies'


class XRay(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='xray', blank=True, null=True)

    class Meta:
        verbose_name = 'X-Ray'
        verbose_name_plural = 'X-Rays'


class Mammography(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='mammography', blank=True, null=True)

    class Meta:
        verbose_name = 'Mammography'
        verbose_name_plural = 'Mammographies'


class Ultrasound(Examination):
    doctor = models.ManyToManyField(Doctor, related_name='ultrasound', blank=True, null=True)

    class Meta:
        verbose_name = 'Ultrasound'
        verbose_name = 'Ultrasound'
        verbose_name_plural = 'Ultrasounds'