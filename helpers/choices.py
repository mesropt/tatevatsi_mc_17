from django.db import models


class GenderChoices(models.TextChoices):
    male = "M", "Male"
    femail = "F", "Female"


class MRIExaminationChoices(models.TextChoices):
    radiosurgery_stereotaxic_mri = (
        "MRI after radiosurgery or stereotaxic interventions",
        "MRI after radiosurgery or stereotaxic interventions",
    )
    breast_mri = "Breast MRI", "Breast MRI"
    spine_mri = "Spine MRI", "Spine MRI"
    brain_mri = "Brain MRI", "Brain MRI"
    joints_mri = "Joints MRI", "Joints MRI"
    arteries_veins_mri = (
        "MRI of arteries and veins",
        "MRI of arteries and veins",
    )
    male_pelvic_mri = "MRI of male pelvic organs", "MRI of male pelvic organs"
    female_pelvic_mri = (
        "MRI of female pelvic organs",
        "MRI of female pelvic organs",
    )
    soft_tissues_mri = "MRI of soft tissues", "MRI of soft tissues"
    abdomen_retroperitoneal_mri = (
        "MRI of abdomen and retroperitoneal space",
        "MRI of abdomen and retroperitoneal space",
    )


# class CTExaminationChoices(models.TextChoices):
#     male = 'M', 'Male'
#     femail = 'F', 'Female'
#
#
# class XRAYExaminationChoices(models.TextChoices):
#     male = 'M', 'Male'
#     femail = 'F', 'Female'
#
#
# class MammographyExaminationChoices(models.TextChoices):
#     male = 'M', 'Male'
#     femail = 'F', 'Female'
#
#
# class UltrasoundExaminationChoices(models.TextChoices):
#     male = 'M', 'Male'
#     femail = 'F', 'Female'
