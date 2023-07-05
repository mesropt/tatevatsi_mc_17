# Generated by Django 4.2.2 on 2023-07-05 15:37

from django.db import migrations, models
import helpers.file_storage


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("examinations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "seniority",
                    models.IntegerField(blank=True, help_text="(years)", null=True),
                ),
                (
                    "scientific_degree",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=helpers.file_storage.doctor_image_storage,
                    ),
                ),
                (
                    "computed_tomography",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="computed_tomography",
                        to="examinations.computedtomography",
                    ),
                ),
                (
                    "magnetic_resonance_imaging",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="magnetic_resonance_imaging",
                        to="examinations.magneticresonanceimaging",
                    ),
                ),
                (
                    "mammography",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="mammography",
                        to="examinations.mammography",
                    ),
                ),
                (
                    "ultrasound",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="ultrasound",
                        to="examinations.ultrasound",
                    ),
                ),
                (
                    "xray",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="xray",
                        to="examinations.xray",
                    ),
                ),
            ],
        ),
    ]
