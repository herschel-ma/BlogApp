from django_registration.forms import RegistrationForm
from .models import userModel


class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = userModel
