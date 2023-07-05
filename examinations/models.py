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
# mri_one_five = MagneticResonanceImaging()
# mri_three = MagneticResonanceImaging()
# mri_contrast_material = MagneticResonanceImaging()
# mri_anesthesia = MagneticResonanceImaging()
# mri_breast = MagneticResonanceImaging()
# mri_heart_one_five = MagneticResonanceImaging()
# mri_heart_three = MagneticResonanceImaging()
#
#
# # ComputedTomography instances:
# ct_computer_layering_polyorgan = ComputedTomography()
# ct_use_of_contrast_material = ComputedTomography()
# ct_one_system_brain = ComputedTomography()
# ct_one_system = ComputedTomography()
# ct_one_system_spine_bones = ComputedTomography()
# ct_paranasal_sinuses = ComputedTomography()
# ct_four_sections_with_ne_contrast = ComputedTomography()
# ct_neuroperfusion = ComputedTomography()
# ct_urological_examination_in_connection_with_nephrolithiasis_without_ne = ComputedTomography()
# ct_angiography_head_neck = ComputedTomography()
# ct_complex_angiography_lower_limb_vessels = ComputedTomography()
# ct_one_system_chest = ComputedTomography()
# ct_two_system_chest = ComputedTomography()
# ct_three_system_chest = ComputedTomography()
# ct_four_system_chest = ComputedTomography()
# ct_dentition_upper_lower_jaws = ComputedTomography()
# ct_abdominal_pelvic_urinary_tract_without_contrast = ComputedTomography()
# ct_temporal_bones = ComputedTomography()
# ct_one_system_anthography = ComputedTomography()
# ct_two_system_anthography = ComputedTomography()
# ct_three_system_anthography = ComputedTomography()
# ct_complex_angiography_lower_limb_vessels_with_abdominal_aorta = ComputedTomography()
# ct_complex_angiography_lower_limb_vessels_with_thoracic_abdominal_aorta = ComputedTomography()
# ct_coronary_arteries_angiography = ComputedTomography()
# ct_coronary_arteries_pulmonary_artery_thoracic_aorta = ComputedTomography()
# ct_coronary_arteries_pulmonary_artery_thoracic_aorta = ComputedTomography()
# ct_aortic_thoracic_abdominal = ComputedTomography()
# ct_neck_brain_arteries = ComputedTomography()
# ct_dentition_layered_examination = ComputedTomography()
# ct_cardiac_angiography = ComputedTomography()
# ct_additional_organ_system = ComputedTomography()
#
# # # XRay
# # name = XRay()
# # name = XRay()
# #
# # # Mammography
# # name = Mammography()
# # name = Mammography()
#
# Ultrasound
# ultra_two_joint_pneu_by_service_head = Ultrasound()
# ultra_lymphatic_system_one_zone_by_service_head = Ultrasound()