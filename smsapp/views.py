from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from .models import StudentModel
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Exists, OuterRef

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response.get("ip")

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "city": response.get("city", "Unknown"),
        "region": response.get("region", "Unknown"),
        "country": response.get("country_name", "Unknown"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    return location_data


def get_weather(latitude, longitude):
    weather_api_key = '81e58cb1ac3fefa0e7e36112ec7d3789'
    if latitude and longitude:
        weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={weather_api_key}')
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temperature = weather_data.get('main', {}).get('temp')
            return temperature
    return None

def home(request):
    if request.user.is_authenticated:
        try:
            ip_address = get_ip()
            location_data = get_location(ip_address)
            latitude, longitude = location_data.get('latitude'), location_data.get('longitude')
            temperature = get_weather(latitude, longitude)
        except Exception as e:
            print(f"Error fetching data: {e}")
            location_data = {
                "city": 'Unknown',
                "region": 'Unknown',
                "country": 'Unknown',
                "latitude": None,
                "longitude": None
            }
            temperature = None

        return render(request, 'home.html', {'location': location_data, 'temperature': temperature})
    else:
        return redirect("ulogin")


def addstudent(request):
    if request.user.is_authenticated:
        error_message = ""
        if request.method == 'POST':
            name = request.POST['name']
            roll_number = request.POST['roll_number']
            marks = request.POST['marks']
            
            roll_number_exists = StudentModel.objects.filter(rno=roll_number).exists()
            if roll_number_exists:
                error_message = "Roll number {} already exists.".format(roll_number)
            else:
                student = StudentModel(name=name, rno=roll_number, marks=marks)
                student.save()
                return redirect('showstudent')
            
        return render(request, 'addstudent.html', {'error_message': error_message})
    else:
        return redirect("ulogin")


def showstudent(request):
	if request.user.is_authenticated:
		students = StudentModel.objects.all()
		return render(request, 'showstudent.html', {'students': students})
	else:
		return redirect("ulogin")

def updatestudent(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            roll_number = request.POST.get('roll_number')
            try:
                student = StudentModel.objects.get(rno=roll_number)
                student.name = request.POST.get('name')
                student.marks = request.POST.get('marks')
                student.save()
                return redirect('showstudent')
            except StudentModel.DoesNotExist:
                error_message = "Student with roll number {} does not exist.".format(roll_number)
                return render(request, 'updatestudent.html', {'error_message': error_message})
        return render(request, 'updatestudent.html')
    else:
        return redirect("ulogin")

def deletestudent(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            roll_number = request.POST.get('roll_number')
            try:
                student = StudentModel.objects.get(rno=roll_number)
                student.delete()
                return redirect('showstudent')
            except ObjectDoesNotExist:
                error_message = "Student with roll number {} does not exist.".format(roll_number)
                return render(request, 'deletestudent.html', {'error_message': error_message})
        return render(request, 'deletestudent.html')
    else:
        return redirect("ulogin")


def ulogin(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw = request.POST.get("pw")
			usr = authenticate(username=un, password=pw)
			if usr is None:
				msg = "Check username/password"
				return render(request,"ulogin.html",{"msg":msg})
			else:
				login(request,usr)
				return redirect("home")
		else:
			return render(request,"ulogin.html")

def usignup(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw1 = request.POST.get("pw1")
			pw2 = request.POST.get("pw2")
			if pw1 == pw2:
				try:
					usr = User.objects.get(username=un)
					msg = "User already exists"
					return render(request,"usignup.html",{"msg":msg})
				except User.DoesNotExist:
					usr = User.objects.create_user(username=un, password=pw1)
					usr.save()
					return redirect("ulogin")
			else:
				msg = "Password did not match"
				return render(request,"usignup.html",{"msg":msg})
		else:
			return render(request,"usignup.html")

def ulogout(request):
	logout(request)
	return redirect("ulogin")






















