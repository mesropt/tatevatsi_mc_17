from django.contrib import admin
from examinations.models import (MagneticResonanceImaging,
                                 ComputedTomography, XRay, Mammography,
                                 Ultrasound)

# Register your models here.
admin.site.register(MagneticResonanceImaging)
admin.site.register(ComputedTomography)
admin.site.register(XRay)
admin.site.register(Mammography)
admin.site.register(Ultrasound)
