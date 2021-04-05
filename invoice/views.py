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


from .models import HistoryCounter, UK, Invoice, House, Street, City, Appartament, User, Services, ConstantPayments, VariablePayments, CurrentCounter


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
        context['const'] = mark_safe(
            serialize('json', ConstantPayments.objects.filter(id=1)))
        context['hist'] = mark_safe(
            serialize('json', HistoryCounter.get_last_val(1)))
        context['curr'] = mark_safe(
            serialize('json', CurrentCounter.get_last_val(1)))
        # get_calc_variable()
        context['test'] = mark_safe(
            serialize('json', VariablePayments.objects.filter(user_id=1).distinct('service')))

        # context['const'] =  mark_safe(json.dumps(get_calc_const(), ensure_ascii=False, default=str))
        return context


# # Расчет КОНСТАНТНЫХ платежей (по сигналу)
# def get_calc_const():
#     users = User.objects.select_related()
#     rate = Services.get_const_payments(1)

#     for user in users:
#         data = dict()
#         for el in rate:
#             if el.unit == 'м2':
#                 data[el.name] = [el.rate * user.appartament.sq_appart, el.unit]
#             elif el.unit == 'чел':
#                 data[el.name] = [el.rate * user.appartament.num_owner, el.unit]
#             else:
#                 data[el.name] = [el.rate, el.unit]
#         user_id = User.objects.get(id=user.id)
#         record = ConstantPayments(user=user_id, data=json.dumps(
#             data, ensure_ascii=False, default=str))
#         record.save()
#     return data


# # Расчет ПЕРЕМЕННЫХ платежей (по сигналу)
# def get_calc_variable():
#     users = User.objects.select_related()
#     curr = CurrentCounter.objects.get(id=1)
#     hist = HistoryCounter.get_last_val(1)[0]
#     rate = Services.get_varybose_payments(1)
    

#     for user in users:
#         data = dict()
#         user_id = User.objects.get(id=user.id)

#         for el in rate:
#             if el.name == 'Холодная вода (индивидуальное потребление)':
#                 value = el.rate * (curr.col_water - hist.hist_col_water )
#             elif el.name == 'Горячая вода (индивидуальное потребление)':
#                 value = el.rate * (curr.hot_water - hist.hist_hot_water )
#             elif el.name == 'Электроэнергия день':
#                 value = el.rate * (curr.electric_day - hist.hist_electric_day )
#             elif el.name == 'Электроэнергия ночь':
#                 value = el.rate * (curr.electric_night - hist.hist_electric_night )
#             record = VariablePayments(user=user_id, period='2021-02-04', service=el.name, price=value)
#             record.save()
