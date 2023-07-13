from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from authnapp.models import CustomUser
from authnapp.forms import CustomUserEditForm, CustomUserLoginForm, CustomUserRegisterForm, UserForm as UserCreationForm, UserUpdateForm
from helpers.mixins import LoginRequiredMixin


def login(request):
    title = "Մուտք"

    login_form = CustomUserLoginForm(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("home:home"))

    content = {"title": title, "login_form": login_form}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("home:home"))


def register(request):
    title = "Գրանցում"

    if request.method == "POST":
        register_form = CustomUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = CustomUserRegisterForm()

    content = {"title": title, "register_form": register_form}
    return render(request, "authnapp/register.html", content)


def edit(request):
    title = "Խմբագրում"

    if request.method == "POST":
        edit_form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = CustomUserEditForm(instance=request.user)

    content = {"title": title, "edit_form": edit_form, "media_url": settings.MEDIA_URL}
    return render(request, "authnapp/edit.html", content)

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'authnapp/profile.html'


class UserListView(ListView):
    model = CustomUser


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
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