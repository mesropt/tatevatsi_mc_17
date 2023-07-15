from django.shortcuts import get_object_or_404, redirect, render

from basket.models import Basket, Product
from examinations.models import (
    ComputedTomography,
    MagneticResonanceImagingOneFiveTesla,
    MagneticResonanceImagingThreeTesla,
    Mammography,
    Ultrasound,
    XRay,
)


def basket(request):
    basket = Basket.objects.filter(user=request.user).first()
    context = {"basket": basket}
    return render(request, "basket/basket.html", context)


def basket_add(request, pk):
    examination = get_object_or_404(
        Examination,
        pk=pk,
        model_type__in=[
            "magneticresonanceimagingthreetesla",
            "magneticresonanceimagingonefivetesla",
            "computedtomography",
            "xray",
            "mammography",
            "ultrasound",
        ],
    )
    basket, created = Basket.objects.get_or_create(user=request.user)
    product, created = Product.objects.get_or_create(
        examination=examination, basket=basket
    )
    product.quantity += 1
    product.save()
    return redirect("basket:view")


def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect("basket:view")
