# from decimal import Decimal
# from django.conf import settings
# from examinations.models import (MagneticResonanceImagingThreeTesla,
#                                   MagneticResonanceImagingOneFiveTesla,
#                                   ComputedTomography, XRay,
#                                  Mammography, Ultrasound)
#
# class Cart:
#     def __init__(self, request):
#     """
#     Инициализировать корзину.
#     """
#     self.session = request.session
#     cart = self.session.get(settings.CART_SESSION_ID)
#     if not cart:
#     # сохранить пустую корзину в сеансе
#     cart = self.session[settings.CART_SESSION_ID] = {}
#     self.cart = cart