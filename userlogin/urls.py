
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index_page'),
    path('register/', views.RegisterView, name='register_page'),
]
