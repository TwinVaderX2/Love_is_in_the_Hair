# information to create registration form found on https://ordinarycoders.com/blog/article/django-user-register-login-logout


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    """
    Class used to create form; used to register new user
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        meta fields used for the registration of new users
        """
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit = True):
        """
        method to commit new user to database
        """
        user = super(NewUserForm, self).save(commit = False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user