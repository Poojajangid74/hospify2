from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=50,default=True)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50,default=True)

    # def __str__(self):
    #     return self.name


class Patient(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=15)
    age = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name


class AdminPanel(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time = models.TimeField()

    # def __str__(self):
    #     return self.doctor.name+"--"+self.patient.name


class PatientDischargeDetails(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)

    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)

    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    OtherCharge = models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)
