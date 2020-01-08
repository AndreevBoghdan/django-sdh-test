from django.urls import path

from . import views

urlpatterns = [
    path('', views.SdhRegistrationView.as_view(), name='register'),
]
