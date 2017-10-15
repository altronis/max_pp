from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ScoreForm
from .models import Score


def index(request):
    return render(request, 'MAXpp/index.html')


def signup_view(request):
    return render(request, 'MAXpp/registration/signup.html')


def signup_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    password_confirm = request.POST['password_confirm']
    if password == password_confirm:
        user = User.objects.create_user(username, 'xx@xx.com', password)
        return render(request, 'MAXpp/index.html', {'user': user})
    else:
        return render(request, 'MAXpp/registration/signup.html', {'error_message': "Passwords do not match."})


def login_view(request):
    return render(request, 'MAXpp/registration/login.html')


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'MAXpp/index.html', {'user': user})
    return render(request, 'MAXpp/registration/login.html', {'error_message': "Invalid username or password."})


def logout_view(request):
    logout(request)
    return render(request, 'MAXpp/registration/logout.html')


def scores_view(request):
    scores_list = Score.objects.filter(player=request.user.username)
    scores_list = scores_list.order_by('pp').reverse()
    return render(request, 'MAXpp/scores.html', {'scores_list': scores_list})


def scores_add(request):
    form = ScoreForm(request.POST)
    if form.is_valid():
        saveform = form.save(commit=False)
        saveform.player = request.user.username
        saveform.save()
        return redirect('/MAXpp/scores/')

    return render(request, 'MAXpp/scores_add.html', {'form': form})
