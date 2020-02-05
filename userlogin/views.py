from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import FormOne, FormTwo, DecisionForm, AttendanceForm
from .models import Applicant, Absent
from django.views import generic
from django.contrib import messages

import smtplib, ssl


def SchoolSelectionView(request, pk):
    try:
        applicant = Applicant.objects.get(pk=pk)
    except Applicant.DoesNotExist:
        raise Http404('Applicant does not exist')
    
    address = applicant.address
    club = applicant.clubs
    """
    using applicant's address and interest/clubs find the most suitable school and assign it to him
    """
    school = 'default : xyz'
    applicant.school = school
    applicant.save()
    message = 'You have been assigned to ' + school + ' school'
    context = {
        'applicant': applicant,
    }
    return render(request, 'userlogin/school_selection.html', context)

def DisplayAbsentView(request):
    queryset = Absent.objects.all()
    context = {
        'queryset' : queryset,
    }
    return render(request, 'userlogin/absent.html', context)

def AttendanceView(request):
    attendance_form = AttendanceForm()

    if request.method == 'POST':
        attendance_form = AttendanceForm(request.POST)
        if attendance_form.is_valid():
            email = attendance_form.cleaned_data.get('email')
            applicant_obj = Applicant.objects.filter(email=email)
            absent_obj = Absent(name=applicant_obj[0].name, email=applicant_obj[0].email, school=applicant_obj[0].school)
            absent_obj.save()
            attendance_form = AttendanceForm()
            messages.success(request, "Your response has been recorded")

    else:
        attendance_form = AttendanceForm()

    context = {
        'form' : attendance_form,
    }
    return render(request, 'userlogin/attendance.html', context)


def ApplicantListView(request):
    queryset = Applicant.objects.filter(score=-1)
    context = {
        'applicant_list' : queryset,
        'title' : 'Applicant List',
    }
    return render(request, 'userlogin/applicant_list.html', context)  


def PhoneInterviewView(request):
    queryset = Applicant.objects.filter(score=0)
    context = {
        'applicant_list' : queryset,
        'title' : 'Phone Interview List',
    }
    return render(request, 'userlogin/applicant_list.html', context)    


def FinalSelectedView(request):
    queryset = Applicant.objects.filter(score=1)
    context = {
        'applicant_list' : queryset,
        'title' : 'Final List/ School Selection',
    }
    return render(request, 'userlogin/applicant_list.html', context)

def ApplicantDetailView(request, pk):
    try:
        applicant = Applicant.objects.get(pk=pk)
    except Applicant.DoesNotExist:
        raise Http404('Applicant does not exist')
    decision_form = DecisionForm()
    
    if request.method == 'POST' :
        decision_form = DecisionForm(request.POST)
        if decision_form.is_valid():
            decision = decision_form.cleaned_data.get('decision')
            print('decision = ', decision)

            redirect_url = ""
            success_message = "generic congrats message"
            if applicant.score == -1:
                redirect_url = 'applicant_list_view'
                success_message = "Congratulations!!! You have passed the first stage. We will contact you about the phone interview timings soon"
            elif applicant.score == 0:
                redirect_url = 'phone_interview_view'
                success_message = "Congratulations!!! You have cleared the phone interview and are selected. We will contact you about the school selection procedure soon"
            elif applicant.score == 1:
                redirect_url = 'final_selected_view'

            print('redirect_url = ', redirect_url)
            if decision == 'Accept':
                applicant.score += 1
                applicant.save()
                # send accepted email
                sendymaily(success_message, applicant.email)

            else :
                applicant.score = -2
                applicant.save()
                failure = "Sorry to infrom you but your application has been rejected. Please consider applying again later"
                #send rejected email
                sendymaily(failure, applicant.email)

            return redirect(redirect_url)
    else:
        decision_form = DecisionForm()

    context = {
        'applicant': applicant,
        'form' : decision_form
    }
    return render(request, 'userlogin/applicant_detail.html', context)



def sendymaily(message, receiver):
    sender = 'sauravjoshi2362000@gmail.com'
    password = 'maxverstappen@33'  
    port = 465

    recieve = receiver
    context = ssl.create_default_context()
    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

    print("sent email!")


def testing(request):
    queryset = Applicant.objects.filter(score=2)
    context = {
        'queryset' : queryset,
    }
    return render(request, "userlogin/testing.html", context)


def FormTwoView(request):
    formtwo = FormTwo()
    if request.method == 'POST':
        formtwo = FormTwo(request.POST)

        if formtwo.is_valid():
            experience = formtwo.cleaned_data.get('experience')
            why_aims = formtwo.cleaned_data.get('why_aims')
            # make a model out of all the available applicant data
            form_data = request.session['form_data']
            Applicant_obj = Applicant.objects.create(
                    email = form_data['email'],
                    name = form_data['name'],
                    phone_number = form_data['phone_number'],
                    clubs = form_data['clubs'],
                    city = form_data['city'],
                    address = form_data['address'],
                    experience = experience,
                    why_aims = why_aims,
            )
            Applicant_obj.save()
            return redirect('accepted_view')

    else :
        formtwo = FormTwo()
    
    context = {
        'form' : formtwo,
    }
    return render(request, 'userlogin/formtwo.html', context)

def FormOneView(request):
    formone = FormOne()
    if request.method == 'POST':
        formone = FormOne(request.POST)
        
        if formone.is_valid():
            email = formone.cleaned_data.get('email')
            name = formone.cleaned_data.get('name')
            phone_number = formone.cleaned_data.get('phone_number')
            clubs = formone.cleaned_data.get('clubs')
            city = formone.cleaned_data.get('city')
            address = formone.cleaned_data.get('address')
            print("clubs = ", clubs)
            print("city = ", city)
            print(type(city))
            if clubs == 'Other' or city == 'Other':
                return render(request, 'userlogin/rejected.html')
            else :
                form_data = {
                    'name' : name,
                    'email' : email,
                    'phone_number' : phone_number,
                    'clubs' : clubs,
                    'city' : city,
                    'address' : address,
                }
                request.session['form_data'] = form_data
                return redirect('form_two_view')
                # return render(request, 'userlogin/accepted.html')
    else:
        formone = FormOne()
    
    context = {
        'form' : formone,
    }
    return render(request, 'userlogin/formone.html', context)

def RejectedView(request):
    return render(request, 'userlogin/rejected.html')

def AcceptedView(request):
    return render(request, 'userlogin/accepted.html')


def index(request):
    return render(request, 'userlogin/index.html')

def dashboard(request):
    return render(request, 'userlogin/dashboard.html')

def RegisterView(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index_page')
    return render(request, 'userlogin/register.html', {'form': form})
