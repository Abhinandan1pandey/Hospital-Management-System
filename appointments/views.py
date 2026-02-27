from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_appointment(request):

    user = request.user

    # Only PATIENT can book
    if user.role != 'PATIENT':
        return Response(
            {"error": "Only patients can book appointments."},
            status=status.HTTP_403_FORBIDDEN
        )

    doctor_id = request.data.get("doctor_id")
    appointment_date = request.data.get("appointment_date")

    try:
        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(user=user)

        appointment = Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_date=appointment_date,
            status="PENDING"
        )

        return Response({
            "message": "Appointment booked successfully",
            "appointment_id": appointment.id
        })

    except Doctor.DoesNotExist:
        return Response(
            {"error": "Doctor not found"},
            status=status.HTTP_404_NOT_FOUND
        )