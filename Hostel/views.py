from multiprocessing import reduction
import re
from django.shortcuts import render ,redirect
from Hostel.models import Boys, Girls
# Create your views here.
def index(request) :
    return render(request,"index.html")

def hostel(request) : 
    total_no_of_boys_seats = 200
    total_no_of_girls_seats = 200
    no_of_boys = 0
    no_of_girls = 0
    boys = Boys.objects.all()
    girls = Girls.objects.all()
    for i in boys :
        no_of_boys = no_of_boys+1
    for i in girls :
        no_of_girls = no_of_girls+1
    total_no_of_boys_seats_available  = total_no_of_boys_seats - no_of_boys
    total_no_of_girls_seats_available  = total_no_of_girls_seats - no_of_girls
    data = {
        'total_no_of_boys_seats' : total_no_of_boys_seats,
        'total_no_of_girls_seats' : total_no_of_girls_seats,
        'total_no_of_boys_seats_available' : total_no_of_boys_seats_available,
        'total_no_of_girls_seats_available' : total_no_of_girls_seats_available,
        'no_of_boys' : no_of_boys,
        'no_of_girls' : no_of_girls
    }
    return render(request,"hostel.html",data)

def admi_form(request) : 
    # if the form is fill by girl
    if request.method == "POST" :
        if request.POST.get("year") == "" or request.POST.get("course") == "" or request.POST.get("gender") == "":
            return redirect("/admi_form")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        mobile_no = request.POST.get("mobile_no")
        parent_mobile_no = request.POST.get("parent_mobile_no")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        address_1 = request.POST.get("address_1")
        address_2 = request.POST.get("address_2")
        college_name = request.POST.get("college_name")
        course = request.POST.get("course")
        year = request.POST.get("year")
        if gender == "male" :
            data = Boys(first_name=first_name,last_name=last_name,mobile_no=mobile_no,parent_mobile_no=parent_mobile_no,gender=gender,email=email,address_1=address_1,address_2=address_2,college_name=college_name,course=course,year=year)
            data.save()
            return redirect("/")
        else :
            data = Girls(first_name=first_name,last_name=last_name,mobile_no=mobile_no,parent_mobile_no=parent_mobile_no,gender=gender,email=email,address_1=address_1,address_2=address_2,college_name=college_name,course=course,year=year)
            data.save()
            return redirect("/")

    return render(request,"admi_form.html")

def mess(request) :
    return render(request,"mess.html")