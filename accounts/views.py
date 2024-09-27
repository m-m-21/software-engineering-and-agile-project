from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup(request):
    try:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('login')  # Redirect to the login page after signup
        else:
            form = CustomUserCreationForm()  # Use your custom form here
        return render(request, 'signup.html', {'form': form})
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'signup.html', {'form': form, 'error': str(e)})

@login_required
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')
