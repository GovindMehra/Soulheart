from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Chore, Star
from .forms import ChoreForm, UserRegistrationForm

@login_required
def chore_list(request):
    chores = Chore.objects.filter(assigned_to=request.user)
    return render(request, 'parents/chore_list.html', {'chores': chores})

@login_required
def add_chore(request):
    if request.method == 'POST':
        form = ChoreForm(request.POST)
        if form.is_valid():
            chore = form.save(commit=False)
            chore.assigned_to = request.user  # Assign current user to chore
            chore.save()
            return redirect('parents/chore_list')
    else:
        form = ChoreForm()
    return render(request, 'parents/add_chore.html', {'form': form})

@login_required
def complete_chore(request, chore_id):
    chore = get_object_or_404(Chore, pk=chore_id)
    chore.is_completed = True
    chore.save()
    Star.objects.create(user=request.user, chore=chore)
    return redirect('parents/chore_list')

@login_required
def delete_chore(request, chore_id):
    chore = get_object_or_404(Chore, pk=chore_id)
    chore.delete()
    return redirect('parents/chore_list')

def index(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'sign_in':
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    error = 'Invalid username or password.'
                    return render(request, 'parents/index.html', {'login_form': login_form, 'signup_form': UserCreationForm(), 'error': error})

        elif form_type == 'sign_up':
            signup_form = UserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'parents/index.html', {'login_form': AuthenticationForm(), 'signup_form': signup_form})
    else:
        login_form = AuthenticationForm()
        signup_form = UserCreationForm()
    return render(request, 'parents/index.html', {'login_form': login_form, 'signup_form': signup_form})
