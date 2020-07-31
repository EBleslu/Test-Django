from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ConnexionForm
from django.contrib.auth.decorators import login_required

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('affichage')
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def affichage(request):
    user = request.user
    return render(request, 'affichage.html', locals())
    