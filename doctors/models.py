from django.db import models
from helpers.choices import GenderChoices
from helpers.file_storage import doctor_image_storage
from examinations.models import Examination


class Doctor(models.Model):
    exam_type = models.ManyToManyField(Examination, related_name='doctor')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    seniority = models.IntegerField()
    scientific_degree = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GenderChoices.choices)
    image = models.ImageField(upload_to=doctor_image_storage, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
