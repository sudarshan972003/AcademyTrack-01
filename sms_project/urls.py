from django.contrib import admin
from django.urls import path
from smsapp.views import ulogin, usignup, ulogout, home, addstudent, showstudent, updatestudent, deletestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",ulogin,name="ulogin"),
    path("usignup",usignup,name="usignup"),
    path("ulogout",ulogout,name="ulogout"),
    path("home",home,name="home"),
    path("addstudent",addstudent,name="addstudent"),
    path("showstudent",showstudent,name="showstudent"),
    path("updatestudent",updatestudent,name="updatestudent"),
    path("deletestudent",deletestudent,name="deletestudent"),
]
