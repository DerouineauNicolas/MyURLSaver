from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from MyURLSaver_app.forms import SignUpForm, AddUrlsForm
from django.shortcuts import render, redirect


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

def addurls(request):
    if request.method == 'POST':
        form = AddUrlsForm(request.POST)
        if form.is_valid():
            form.save()
            url = form.cleaned_data.get('urls')
            request.user.add_url(url)
    else:
        form = AddUrlsForm()
    return render(request, 'urls.html', {'form': form})
