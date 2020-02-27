from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__( *args, **kargs)

    class Meta:
        CustomUser = get_user_model()

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(self.error_message['duplicate_username'])
