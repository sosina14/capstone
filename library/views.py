from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in automatically
            return redirect('home')  # Change 'home' to your actual homepage URL name
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
