from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class ExtendedUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['last_name'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Userfields = ['username', 'first_name', 'last_name', 'password1', 'password2']
