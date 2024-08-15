from django.db import models

class Invoice(models.Model):
    client_name = models.CharField(max_length=255, verbose_name="Client Name")
    invoice_number = models.CharField(max_length=50, unique=True, verbose_name="Invoice Number")
    date = models.DateField(verbose_name="Date")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount")
    project_name = models.CharField(max_length=255, verbose_name="Project Name")
    project_description = models.TextField(verbose_name="Project Description")
    project_address = models.CharField(max_length=255, verbose_name="Project Address")
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Estimated Budget")
    total_amount_spent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount Spent")
    estimated_project_duration = models.IntegerField(verbose_name="Estimated Project Duration")

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client_name}"
