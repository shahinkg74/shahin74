from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'از حساب کاربری خود خارج شدید', 'success')
        return redirect('home:home')
