from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials.'})
    else:
        return render(request, 'login.html')


class user_registration(View):
    @staticmethod
    def get(request):
        return redirect('/')

    @staticmethod
    def post(self, request):
        return redirect('/')


class user_info_change(View):
    @staticmethod
    def get(request):
        return redirect('/')

    @staticmethod
    def post(self, request):
        return redirect('/')

def home(request):
    return render(request, 'home.html')
