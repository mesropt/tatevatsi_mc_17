from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from helpers.mixins import LoginRequiredMixin
from users.forms import UserForm as UserCreationForm, UserUpdateForm


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            user = form.save()
            user.profile.phone = phone
            user.profile.save()
            messages.success(request, f'User with {user.username} username created successfully')
            return redirect('home')
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')
    return render(request, 'users/login.html', {})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Successfully loging out')
    return redirect('home')


class UserDetailView(DetailView):
    model = User


class UserListView(ListView):
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.get_object().pk})

    def get_form_kwargs(self):
        user = self.get_object()
        kwargs = super().get_form_kwargs()
        kwargs.update({'initial': {'phone': user.profile.phone,
                                   'photo': user.profile.photo}})
        return kwargs

    def form_valid(self, form):
        user = self.get_object()
        phone = form.cleaned_data.get('phone')
        photo = form.cleaned_data.get('photo')
        user.profile.phone = phone
        user.profile.photo = photo
        user.profile.save()
        return super().form_valid(form)
