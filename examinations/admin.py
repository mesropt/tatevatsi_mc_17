from django.contrib import admin
from examinations.models import (MagneticResonanceImagingOneFiveTesla, MagneticResonanceImagingThreeTesla,
                                 ComputedTomography, XRay, Mammography,
                                 Ultrasound)

class MagneticResonanceImagingOneFiveTeslaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')
    filter_horizontal = ('doctor',)

class MagneticResonanceImagingThreeTeslaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')
    filter_horizontal = ('doctor',)

class ComputedTomographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')
    filter_horizontal = ('doctor',)


class XRayAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')
    filter_horizontal = ('doctor',)


class MammographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')
    filter_horizontal = ('doctor',)


class UltrasoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')
    filter_horizontal = ('doctor',)


admin.site.register(MagneticResonanceImagingOneFiveTesla, MagneticResonanceImagingOneFiveTeslaAdmin)
admin.site.register(MagneticResonanceImagingThreeTesla, MagneticResonanceImagingThreeTeslaAdmin)
admin.site.register(ComputedTomography, ComputedTomographyAdmin)
admin.site.register(XRay, XRayAdmin)
admin.site.register(Mammography, MammographyAdmin)
admin.site.register(Ultrasound, UltrasoundAdmin)
