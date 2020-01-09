from json import dumps as json_dumps

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.forms import CharField, ValidationError

from .models import Profile
from .forms import UserForm
from .utils import generate_invitation_code

from django_registration.backends.activation.views import RegistrationView, ActivationView

# Create your views here.

class SdhRegistrationView(RegistrationView):
    def get(self, request):
        registrationForm = UserForm()
        return render(request, 'registration/registration_form.html', {'form': registrationForm})

    def post(self,request):
        requestArray = request.POST
        form = UserForm(requestArray, instance=User()) 
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            inviter_profile = Profile.objects.filter(invitation_code=form.cleaned_data['invitation_code']).first()
            #raise ValidationError( form.cleaned_data['invitation_code'] )
            new_profile = Profile.objects.create(user=new_user, inviter=inviter_profile.user)
            self.send_activation_email(new_user)
            if request.is_ajax():
                return HttpResponse("OK")
            else:
                return redirect(reverse_lazy("django_registration_complete"))
        else:
            return HttpResponseBadRequest(json_dumps(form.errors))

class SdhActivationView(ActivationView):
    success_url = reverse_lazy("user_profile")

    def activate(self, *args, **kwargs):
        username = self.validate_key(kwargs.get("activation_key"))
        user = self.get_user(username)
        user.is_active = True
        user.save()
        login(self.request, user)
        return user

@login_required
def profile(request):
    args = {}
    user = request.user
    profile = user.profile
    args['user_profile'] = profile
    args['user_referals'] = Profile.objects.filter(inviter=user)
    return render(request, 'registration/profile.html', args)

@login_required
def generate_new_code(request):
    profile = request.user.profile
    profile.invitation_code = generate_invitation_code()
    profile.save()
    return HttpResponse(json_dumps({"new_code": profile.invitation_code}))

#utils