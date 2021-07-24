from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from petstagram_django.accounts.forms import LoginForm


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = LoginForm
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def register_user(request):
    pass


def logout_user(request):
    logout(request)
    return redirect('landing page')
