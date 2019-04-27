from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if request.user.is_authenticated:

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                context['form'] = LoginForm()
                messages.success(request, f' {username} Successfully LOG IN !')
                return redirect('blog-home')
            else:
                messages.error(request, " Invalid Password or UserName")
                return redirect('/login_page')

    return render(request, 'users/login.html', context)