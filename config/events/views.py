# events/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventRegistrationForm

def register_event(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('.') 
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EventRegistrationForm()
    
    return render(request, 'events/register.html', {'form': form})