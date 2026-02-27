from django.db import models
from accounts.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    experience_years = models.IntegerField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Dr. {self.user.username}"