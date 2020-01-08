from json import dumps as json_dumps

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.models import User

from .forms import UserForm

from django_registration.backends.activation.views import RegistrationView

# Create your views here.

"""
def register(request):
    if request.method=="POST":

    else:
        registrationForm = UserForm()
        return render(request, 'registration/registration_form.html', {'form': registrationForm})
    return 'OK';"""



class SdhRegistrationView(RegistrationView):
    def get(self, request):
        registrationForm = UserForm()
        return render(request, 'registration/registration_form.html', {'form': registrationForm})

    def post(self,request):
        requestArray = request.POST
        #requestArray['is_active'] = False
        form = UserForm(requestArray, instance=User()) 
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            self.send_activation_email(new_user)
            if request.is_ajax():
                return HttpResponse("OK")
            else:
                return redirect(reverse_lazy("django_registration_complete"))
        else:
            return HttpResponseBadRequest(json_dumps(form.errors))

#utils