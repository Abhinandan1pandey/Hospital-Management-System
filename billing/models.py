from django.db import models
from appointments.models import Appointment


class Invoice(models.Model):

    PAYMENT_STATUS = (
        ('UNPAID', 'Unpaid'),
        ('PAID', 'Paid'),
    )

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)

    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    additional_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='UNPAID')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.consultation_fee + self.additional_charges
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice for {self.appointment.patient.user.username}"