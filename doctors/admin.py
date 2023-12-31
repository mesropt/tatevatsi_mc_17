from django.contrib import admin

from doctors.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    list_filter = ("gender",)
    search_fields = ("first_name", "last_name")
    # fields = ['doctors']
    fieldsets = (
        (
            "Doctor",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "gender",
                    "seniority",
                    "specialization",
                    "scientific_degree",
                    "university",
                    "date_of_birth",
                    "image",
                )
            },
        ),
    )
    filter_horizontal = (
        "magnetic_resonance_imaging_1_5t",
        "magnetic_resonance_imaging_3t",
        "computed_tomography",
        "computed_tomography",
        "xray",
        "mammography",
        "ultrasound",
    )


admin.site.register(Doctor, DoctorAdmin)
