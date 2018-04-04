from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from MyURLSaver_app.forms import SignUpForm, AddUrlsForm
from django.shortcuts import render, redirect
from MyURLSaver_app.models import URL
from django.http import HttpResponse


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def addurls(request):
    if request.method == 'POST':
        form = AddUrlsForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            request.user.add_url(url)
            return redirect('home')
    else:
        form = AddUrlsForm()
    return render(request, 'urls.html', {'form': form})

@login_required
def seeurls(request):
    if request.method == 'POST':
        return HttpResponseForbidden()
    else:
        return render(request, 'seeurls.html')

@login_required
def delurls(request):
    if request.method == 'POST':
        form = AddUrlsForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
        request.user.del_url(url)
        return HttpResponse(status=204)
    else:
        return HttpResponseForbidden()
