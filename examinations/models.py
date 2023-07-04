from django.db import models
# from helpers.file_storage import movie_images_storage, producer_images_storage
from django.core.exceptions import ValidationError
from abc import ABCMeta, abstractmethod


# def validate_rate(value):
#     if value > 10:
#         raise ValidationError('Value can not be more than 10')
#     return value


class Examination(models.Model, metaclass=ABCMeta):
    # mri = models.CharField(max_length=50, choices=MRIExaminationChoices.choices)
    # ct = models.CharField(max_length=50, choices=CTExaminationChoices.choices)
    # x_ray = models.CharField(max_length=50, choices=XRAYExaminationChoices.choices)
    # mammography = models.CharField(max_length=50, choices=MammographyExaminationChoices.choices)
    # ultrasound = models.CharField(max_length=50, choices=UltrasoundExaminationChoices.choices)
    # producer = models.ForeignKey('Producer', on_delete=models.CASCADE)
    # name = models.CharField(max_length=150)
    # year = models.IntegerField()
    # rate = models.FloatField(null=True, blank=True, validators=[validate_rate])
    # description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(null=True, blank=True, upload_to=movie_images_storage)

    # def __str__(self):
    #     return self.mri

    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

class MagneticResonanceImaging(Examination):
    pass

class ComputedTomography(Examination):
    pass

class XRay(Examination):
    pass


class Mammography(Examination):
    pass

class Ultrasound(Examination):
    pass


# SUBCLASSES
class MRIOneFive(MagneticResonanceImaging):
    pass

class MRIThree(MagneticResonanceImaging):
    pass

class MRIContrastMaterial(MagneticResonanceImaging):
    pass

class MRIAnesthesia(MagneticResonanceImaging):
    pass

class MRIBreast(MagneticResonanceImaging):
    pass

class MRIHeartOneFive(MagneticResonanceImaging):
    pass


class MRIHeartThree(MagneticResonanceImaging):
    pass