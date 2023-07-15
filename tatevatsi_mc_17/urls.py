from allauth.account.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('basket/', include('basket.urls', namespace='basket')),
    # path('cart/', include('cart.urls', namespace='cart')),
    path(
        "examinations/", include("examinations.urls", namespace="examinations")
    ),
    path("doctors/", include("doctors.urls", namespace="doctors")),
    path("auth/", include("authnapp.urls", namespace="auth")),
    path("", include("home.urls", namespace="home")),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
