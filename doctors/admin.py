from django.contrib import admin
from doctors.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name')
    fieldsets = (('Doctor', {'fields': ('first_name', 'last_name', 'gender',
                                        'seniority', 'scientific_degree',
                                        'date_of_birth', 'image')}),
                ('MagneticResonanceImagingOneFiveTesla', {'fields': ('magnetic_resonance_imaging_1_5t',)}),
                 ('MagneticResonanceImagingThreeTesla', {'fields': ('magnetic_resonance_imaging_3t',)}),
                 ('ComputedTomography', {'fields': ('computed_tomography',)}),
                 ('XRay', {'fields': ('xray',)}),
                 ('Mammography', {'fields': ('mammography',)}),
                 ('Ultrasound', {'fields': ('ultrasound',)}))
    filter_horizontal = ('magnetic_resonance_imaging_1_5t', 'magnetic_resonance_imaging_3t', 'computed_tomography', 'computed_tomography', 'xray', 'mammography', 'ultrasound',)


admin.site.register(Doctor, DoctorAdmin)

