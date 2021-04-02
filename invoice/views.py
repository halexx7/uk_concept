from django.conf import settings
from django.contrib.postgres import fields
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from django.utils.safestring import mark_safe
import json


from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView


from .models import UK, Invoice, House, Street, City, Appartament, User, Services, ConstantPayments, VariablePayments


def main(request):

    invoice = mark_safe(serialize('json', User.objects.filter(pk=1)))
    return render(request, "invoice/main.html", context={'data': invoice})


# class InvoiceViews(ListView):
#     context_object_name = 'user'
#     template_name = 'invoice/main.html'
#     queryset = mark_safe(serialize('json', User.objects.filter(pk=1)))

#     def get_context_data(self, **kwargs):
#         context = super(InvoiceViews, self).get_context_data(**kwargs)
#         context['appartaments'] = mark_safe(serialize('json', Appartament.objects.all()))
#         context['house'] = mark_safe(serialize('json', House.objects.all()))
#         context['city'] = mark_safe(serialize('json', City.objects.all()))
#         context['street'] = mark_safe(serialize('json', Street.objects.all()))
#         context['uk'] = mark_safe(serialize('json', UK.objects.all()))
#         context['invoice'] = mark_safe(serialize('json', Invoice.objects.all()))
#         return context


# class InvoiceViews2(ListView):
#     context_object_name = 'user'
#     template_name = 'invoice/main.html'
#     queryset = User.objects.filter(pk=1)

#     def get_context_data(self, **kwargs):
#         context = super(InvoiceViews, self).get_context_data(**kwargs)
    
#         context["const_pay"] = mark_safe(serialize('json', ConstantPayments.get_items(self.request.user)))
#         context["variable_pay"] = mark_safe(serialize('json', VariablePayments.get_items(self.request.user)))
    
#         return context



# class InvoiceViews(ListView):
#     model = User

#     def get_context_data(self, **kwargs):
#         pass

class InvoiceViews(ListView):
    context_object_name = 'user'
    template_name = 'invoice/main.html'
    queryset = mark_safe(serialize('json', User.objects.filter(pk=1)))

    def get_context_data(self, **kwargs):
        context = super(InvoiceViews, self).get_context_data(**kwargs)
        context['const'] =  mark_safe(json.dumps(get_calc_const(), ensure_ascii=False, default=str))
        return context


def get_calc_const():
    users = User.objects.select_related()
    rate = Services.get_const_payments(1)

    for user in users:
        data = dict()
        for el in rate:
            if el.unit == 'м2':
                data[el.name] = [el.rate * user.appartament.sq_appart, el.unit]
            elif el.unit == 'чел':
                data[el.name] = [el.rate * user.appartament.num_owner, el.unit]
            else:
                data[el.name] = [el.rate, el.unit]
    return data