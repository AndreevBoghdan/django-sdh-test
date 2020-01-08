from django.conf import settings

from django.forms.models import modelformset_factory
from django.forms import CharField, ValidationError
from django.forms.widgets import TextInput

from django.contrib.auth.models import User

from django_registration.forms import RegistrationForm


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
            return data['invitation_code']