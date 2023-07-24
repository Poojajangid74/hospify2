from django.contrib.auth import logout
from django.forms import forms, models
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

from info_hospy.models import Patient, AdminPanel, Doctor, Appointment


# Create your views here.
#
def registration(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    address = request.POST.get('address')
    state = request.POST.get('state')
    city = request.POST.get('city')

    if not name:
        return HttpResponse("Name field cannot be empty")

    try:
        Patient.objects.get(email=email)
        return HttpResponse("you are already a user please login")
    except Patient.DoesNotExist:
        pass

    user1 = Patient(name=name, email=email, mobile=mobile, gender=gender, age=age,
                    state=state, address=address, city=city)

    user1.save()
    return HttpResponse('completed')


# def registration(request):
#     name = request.GET.get('name')
#     email = request.GET.get('email')
#     mobile = request.GET.get('mobile')
#     gender = request.GET.get('gender')
#     age = request.GET.get('age')
#     address = request.GET.get('address')
#     state = request.GET.get('state')
#     city = request.GET.get('city')
#
#     if not name:
#         return HttpResponse("Name field cannot be empty")
#
#     try:
#         Patient_Info.objects.get(email=email)
#         return HttpResponse("you are already a user please login")
#     except Patient_Info.DoesNotExist:
#         pass
#
#     user1 = Patient_Info(name=name, email=email, mobile=mobile, gender=gender, age=age,
#                          state=state, address=address, city=city)
#
#     user1.save()
#     return HttpResponse('completed')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            Patient.objects.get(email=email)
        except Patient.DoesNotExist:
            return HttpResponse('please enter a valid email-id')

    return HttpResponse('welcome')


def Logout(request):
    if not request.user.is_staff:
        return HttpResponse("login")
    logout(request)
    return HttpResponse('login')


def update_patient_info(request):

    # id = request.GET['id']

    try:
        id = request.GET.get('id')
        patient = Patient.objects.get(id=id)

    except Patient.DoesNotExist:
               return HttpResponseBadRequest("Invalid id")

    # Update job fields if provided in request
    if 'name' in request.GET:
        patient.name = request.GET['name']
        print(patient.name)
    if 'email' in request.GET:
        patient.email = request.GET['email']
    if 'age' in request.GET:
        patient.age = request.GET['age']
    if 'mobile' in request.GET:
        patient.mobile = request.GET['mobile']
    if 'address' in request.GET:
        patient.address = request.GET['address']
    if 'state' in request.GET:
        patient.state = request.GET['state']
    if 'city' in request.GET:
        patient.city = request.GET['city']
    if 'gender' in request.GET:
        patient.gender = request.GET['gender']

    patient.save()
    return HttpResponse('updated successfully')


def delete_patient(request, myid):
    patient = Patient.objects.filter(id=myid)
    patient.delete()
    return HttpResponse('successfully deleted')



def doctor_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

    admin = AdminPanel(username=username, email=email, password=password)
    admin.save()
    return HttpResponse('completed')

def doctor_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            AdminPanel.objects.get(email=email)
        except AdminPanel.DoesNotExist:
            return HttpResponse('please enter a valid email-id')

        try:
            AdminPanel.objects.get(password=password)
        except AdminPanel.DoesNotExist:
            return HttpResponse('please enter a valid password')

    return HttpResponse('welcome')


def delete_doctor(request):
    doctor = Doctor.objects.filter(id=id)
    doctor.delete()
    return HttpResponse('successfully deleted')

def Index(request):
    if not request.user.is_staff:
        return HttpResponse('login')
def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return HttpResponse('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error = 'no'
        except:
            error = 'yes'
    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return HttpResponse('add_appointment successfully')


def Delete_Appointment(request):
    if not request.user.is_staff:
        return HttpResponse('login')




