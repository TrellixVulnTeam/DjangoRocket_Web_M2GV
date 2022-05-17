from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from account.models import Organization, User, Team
from django.utils.translation import gettext_lazy as _

class OrganiztionForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['org_name']
        labels = {
            'org_name': _('Organiztion')
        }
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name')
        }
        
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name']



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None