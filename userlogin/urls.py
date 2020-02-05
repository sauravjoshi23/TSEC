
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('register/', views.RegisterView, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='userlogin/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='userlogin/logout.html'), name='logout'),
    path('formone/', views.FormOneView, name='form_one_page'),
    path('accepted/', views.AcceptedView, name='accepted_page'),
    path('rejected/', views.RejectedView, name='rejected_page'),
]
