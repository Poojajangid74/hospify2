from django.urls import path

from info_hospy import views, admin
from info_hospy.views import registration, user_login, update_patient_info, delete_patient, doctor_login, Logout, \
    delete_doctor, Add_Appointment, Delete_Appointment, doctor_signup

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('registration/',registration),
    path('user_login/',user_login),
    path('logout/',Logout,name="login"),
    path('update/',update_patient_info),
    path("delete_patient/<int:myid>/", delete_patient, name="delete_patient"),
    path( 'doctor_signup/', doctor_signup),
    path('doctor_login/',doctor_login),
    path('delete_doctor/<int:myid/',delete_doctor),
    path('add_appointment/',Add_Appointment,name='add_appointment'),
    path('delete_appointment/',Delete_Appointment),



]