from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Invoice
from .forms import InvoiceForm

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice_list.html'
    context_object_name = 'invoices'

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice_form.html'
    success_url = '/invoices/'

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice_detail.html'
