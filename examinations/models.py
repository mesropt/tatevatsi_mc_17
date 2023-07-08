from django.db import models
from abc import abstractmethod
from helpers.file_storage import examination_images_storage

# ABSTRACT CLASS:
class Examination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    doctor = models.ManyToManyField('Doctor', related_name='examinations', null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=examination_images_storage)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

    @abstractmethod
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
        verbose_name_plural = 'Ultrasounds'

#
# # INSTANCES:
# # MRI instances:auth_user_user_permissions
# Spine MRI(1.5T) one part = MagneticResonanceImaging()
# Spine MRI(3T) one part = MagneticResonanceImaging()
# Brain MRI(1.5T) = MagneticResonanceImaging()
# Brain MRI(3T) = MagneticResonanceImaging()
# Breast MRI(1.5T) = MagneticResonanceImaging()
# Breast MRI(3T) = MagneticResonanceImaging()
# Joints MRI(1.5T) = MagneticResonanceImaging()
# Joints MRI(3T) = MagneticResonanceImaging()
# MRI of abdomen and retroperitoneal space(1.5T) = MagneticResonanceImaging()
# MRI of abdomen and retroperitoneal space(3T) = MagneticResonanceImaging()
# MRI of soft tissues (1.5T) = MagneticResonanceImaging()
# MRI of soft tissues (3T) = MagneticResonanceImaging()
# MRI of arteries and veins (1.5T) = MagneticResonanceImaging()
# MRI of arteries and veins (3T) = MagneticResonanceImaging()
# Contrast_material (1.5T) = MagneticResonanceImaging()
# Contrast_material (3T) = MagneticResonanceImaging()


#
#
# # ComputedTomography instances:
# ct_computer_layering_polyorgan = ComputedTomography()
# ct_use_of_contrast_material = ComputedTomography()
# ct_one_system_brain = ComputedTomography()
# ct_one_system_spine_bones = ComputedTomography()
# ct_paranasal_sinuses = ComputedTomography()
# ct_complex_angiography_lower_limb_vessels = ComputedTomography()
# ct_one_system_chest = ComputedTomography()
# ct_two_system_chest = ComputedTomography()
# ct_dentition_upper_lower_jaws = ComputedTomography()
# ct_abdominal_pelvic_urinary_tract_without_contrast = ComputedTomography()
# ct_temporal_bones = ComputedTomography()
# ct_one_system_anthography = ComputedTomography()
# ct_two_system_anthography = ComputedTomography()
# ct_three_system_anthography = ComputedTomography()
# ct_coronary_arteries_angiography = ComputedTomography()
# ct_aortic_thoracic_abdominal = ComputedTomography()
# ct_neck_brain_arteries = ComputedTomography()
# ct_cardiac_angiography = ComputedTomography()
# ct_additional_organ_system = ComputedTomography()
#
# # # XRay
# Abdominal x-ray
# Bone x-ray
# Chest x-ray
# Dental x-ray
# Extremity x-ray
# Joint x-ray
# Spine x-ray
# Lungs X-ray
# Skull X-Ray
# Hand X-Ray
# Kidney, Ureter and Bladder X-Ray
# Neck X-Ray
# # # name = XRay()
# # name = XRay()
# #
# # # Mammography
# Mammography
# # name = Mammography()
# # name = Mammography()
#
# Ultrasound
#     Heart and blood vessels, including the abdominal aorta and its major branches
#     Liver
#     Mammary glands
#     Brain
#     spleen
#     Pelvic organs
#     Internal organs
#     kidneys
#     Abdominal organs
#     uterus, ovaries, and unborn child (fetus) in pregnant patients