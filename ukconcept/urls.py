from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from invoice import views
from django.contrib import admin
import invoice.views as invoice

urlpatterns = [
    path("admin/", admin.site.urls),
    path('invoice/', invoice.InvoiceViews.as_view(), name='invoice'),
    path("auth/", include("authnapp.urls", namespace="auth")),
    # path('invoice/', invoice.main, name='invoice'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()