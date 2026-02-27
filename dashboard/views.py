from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment
from billing.models import Invoice


@login_required
def dashboard(request):

    user = request.user

    # ADMIN
    if user.is_superuser:
        context = {
            "total_doctors": Doctor.objects.count(),
            "total_patients": Patient.objects.count(),
            "total_appointments": Appointment.objects.count(),
            "total_revenue": Invoice.objects.all().count(),
        }
        return render(request, "admin_dashboard.html", context)


    # DOCTOR
    if hasattr(user, 'doctor'):
        appointments = Appointment.objects.filter(doctor=user.doctor)
        context = {
            "appointments": appointments,
            "total": appointments.count(),
        }
        return render(request, "doctor_dashboard.html", context)


    # PATIENT
    if hasattr(user, 'patient'):
        appointments = Appointment.objects.filter(patient=user.patient)
        context = {
            "appointments": appointments,
            "total": appointments.count(),
        }
        return render(request, "patient_dashboard.html", context)


    # DEFAULT
    return render(request, "base.html")