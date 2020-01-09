from django.conf import settings

from django.forms.models import modelformset_factory
from django.forms import CharField, ValidationError, ModelForm
from django.forms.widgets import TextInput

from django.contrib.auth.models import User

from django_registration.forms import RegistrationForm

from .models import Profile


class UserForm(RegistrationForm):
    invitation_code = CharField(widget=TextInput,
                        required=False,
                        label=("Invitation Code"))
    class Meta:
        model = User
        fields = ['username',  'email', 'password1', 'password2', 'invitation_code']

    def clean_invitation_code(self):
        data = self.cleaned_data
        if not data['invitation_code']:
                usersNumber = User.objects.all().count();
                if (usersNumber > settings.USERS_WITHOUT_CODE):
                    raise ValidationError(('This field is required'))
        else:
            if (Profile.objects.filter(invitation_code=data['invitation_code']).count() == 0):
                raise ValidationError(('Your Invitation Code Is Not Valid'))
            return data['invitation_code']

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['invitation_code']
