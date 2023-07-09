from django.db import models
from helpers.file_storage import examination_images_storage





class Equipment(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    doctor = models.ManyToManyField('Doctor', related_name='equipments', null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=examination_images_storage)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @abstractmethod
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    equipment = models.ManyToManyField(Equipment, related_name='doctors',
                                       blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'