from django.conf import settings
from django.contrib.postgres import fields
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from django.utils.safestring import mark_safe


from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView


from .models import UK, Invoice, House, Street, City, Appartament, User, ConstantPayments, VariablePayments


def main(request):

    invoice = mark_safe(serialize('json', User.objects.filter(pk=1)))
    return render(request, "invoice/main.html", context={'data': invoice})


class InvoiceViews(ListView):
    context_object_name = 'user'
    template_name = 'invoice/main.html'
    queryset = mark_safe(serialize('json', User.objects.filter(pk=1)))

    def get_context_data(self, **kwargs):
        context = super(InvoiceViews, self).get_context_data(**kwargs)
        context['appartaments'] = mark_safe(serialize('json', Appartament.objects.all()))
        context['house'] = mark_safe(serialize('json', House.objects.all()))
        context['city'] = mark_safe(serialize('json', City.objects.all()))
        context['street'] = mark_safe(serialize('json', Street.objects.all()))
        context['uk'] = mark_safe(serialize('json', UK.objects.all()))
        context['invoice'] = mark_safe(serialize('json', Invoice.objects.all()))
        return context


# class InvoiceViews2(ListView):
#     context_object_name = 'user'
#     template_name = 'invoice/main.html'
#     queryset = User.objects.filter(pk=1)

#     def get_context_data(self, **kwargs):
#         context = super(InvoiceViews, self).get_context_data(**kwargs)
    
#         context["const_pay"] = mark_safe(serialize('json', ConstantPayments.get_items(self.request.user)))
#         context["variable_pay"] = mark_safe(serialize('json', VariablePayments.get_items(self.request.user)))
    
#         return context