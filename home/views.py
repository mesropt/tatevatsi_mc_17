# from django.db import models
# from doctors.views import Doctors
#
#
# class Doctor(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Company'
#         verbose_name_plural = 'Companies'
#
#
# class MagneticResonanceImaging(models.Model):
#     name = models.CharField(max_length=255)
#     doctors = models.OneToMany(Doctors, on_delete=models.CASCADE,
#                                 related_name='pizza'
#     mri_exam_type = models.CharField(max_length=10, choices=MRIExamTypeChoices.choices)
#     description = models.TextField()
#     image = models.ImageField(upload_to=upload_mri_image)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
