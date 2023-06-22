from django import forms

from MyMusic.account.models import UserModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
