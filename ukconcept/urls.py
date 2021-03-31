from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from invoice import views
import invoice.views as invoice

urlpatterns = [
    path('invoice/', invoice.InvoiceViews.as_view(), name='invoice'),
    # path('invoice/', invoice.main, name='invoice'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()