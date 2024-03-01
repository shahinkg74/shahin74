from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_("رمز عبور"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("تکرار رمز عبور"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone', 'username', 'fullname', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password2'] != cd['password1']:
            raise ValidationError("Passwords don't match")
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text=_("تو میتونی رمز عبور را عوض کنی با استفاده از <a href=\"../password/\">این فرم</a>")
    )

    class Meta:
        model = User
        fields = (
            'phone', 'username', 'fullname', 'email', 'password', 'is_active', 'is_admin'
        )
