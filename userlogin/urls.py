
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('', views.index, name='index_page'),
    path('register/', views.RegisterView, name='register_page'),
]
