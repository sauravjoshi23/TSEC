from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import FormOne, FormTwo, DecisionForm
from .models import Applicant
from django.views import generic

import smtplib


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
            if applicant.score == -1:
                redirect_url = 'applicant_list_view'
            elif applicant.score == 0:
                redirect_url = 'phone_interview_view'
            elif applicant.score == 1:
                redirect_url = 'final_selected_view'

            print('redirect_url = ', redirect_url)
            if decision == 'Accept':
                applicant.score += 1
                applicant.save()
                # send accepted email
                email = applicant.email
                message = "You have passed the first stage. Prepare fot the phone interview"
                

            else :
                applicant.score = -2
                applicant.save()
                #send rejected email


            return redirect(redirect_url)
    else:
        decision_form = DecisionForm()

    context = {
        'applicant': applicant,
        'form' : decision_form
    }
    return render(request, 'userlogin/applicant_detail.html', context)


def sendymaily(content, receiver):
    print('inside sendy maily')
    mail = smtplib.SMTP('smtp.rediff.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('sj2362000@rediff.com','Abcde123@')
    mail.sendmail('sj2362000@rediff.com',receiver,content)
    mail.close()


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
