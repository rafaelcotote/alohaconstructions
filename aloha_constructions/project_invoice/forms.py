from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'client_name', 'invoice_number', 'date', 'total_amount', 
            'project_name', 'project_description', 'project_address', 
            'estimated_budget', 'total_amount_spent', 'estimated_project_duration'
        ]
