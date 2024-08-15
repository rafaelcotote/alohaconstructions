from django.db import models
from django.contrib.auth.models import User
from project_base.models import CadastroProjeto
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class CheckinRegister(models.Model):
    CHECKIN = 'Check-in'
    CHECKOUT = 'Check-out'
    TYPE_CHOICES = [
        (CHECKIN, 'Check-in'),
        (CHECKOUT, 'Check-out'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(CadastroProjeto, on_delete=models.CASCADE)
    date_register = models.DateTimeField(blank=False)
    activity = models.TextField(null=False, blank=True, verbose_name='Activity',)
    check_out = models.DateTimeField(blank=True, null=True)
    hours_worked = models.FloatField(blank=True, null=True)
    type_register = models.CharField(max_length=10, choices=TYPE_CHOICES, default=CHECKIN)

    def __str__(self):
        return "{} - {} ({})".format(self.employee, self.project, self.date_register)

@receiver(pre_save, sender=CheckinRegister)
def update_check_out(sender, instance, **kwargs):
    existing_checkins = CheckinRegister.objects.filter(
        employee=instance.employee,
        project=instance.project,
        date_register__date=instance.date_register.date(),
    ).order_by('date_register')

    last_checkin = existing_checkins.last()

    if instance.type_register == CheckinRegister.CHECKIN:
        # Update the last check-in if there's any
        if last_checkin:
            last_checkin.check_out = instance.date_register
            last_checkin.type_register = CheckinRegister.CHECKOUT
            last_checkin.hours_worked = (instance.date_register - last_checkin.date_register).total_seconds() / 3600
            last_checkin.save()

    # Always set check_out to None for new check-in records
    instance.check_out = None

@receiver(post_save, sender=CheckinRegister)
def set_check_out(sender, instance, created, **kwargs):
    if created and instance.check_out is None:
        instance.check_out = instance.date_register
        instance.type_register = CheckinRegister.CHECKOUT
        instance.hours_worked = 0  # Set to 0 for first check-in
        instance.save()

    if instance.type_register == CheckinRegister.CHECKOUT:
        # Calculate hours worked for check-out records
        checkin = CheckinRegister.objects.filter(
            employee=instance.employee,
            project=instance.project,
            date_register__date=instance.date_register.date(),
            type_register=CheckinRegister.CHECKIN
        ).order_by('date_register').last()

        if checkin:
            instance.hours_worked = (instance.date_register - checkin.date_register).total_seconds() / 3600
            instance.save()
