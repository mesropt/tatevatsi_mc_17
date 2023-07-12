from django.contrib.auth import login, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from users.forms import UserForm as UserCreationForm, UserUpdateForm
from helpers.mixins import LoginRequiredMixin

from users.forms import EmailForm, RegistrationForm
from django.conf import settings
from users.models import User

from users.token_generator import account_activation_token

User = get_user_model()


class UserTemplateView(TemplateView):
    template_name = 'user_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.first()
        send_mail(subject="Custom user model", message='The best students ever',
                  recipient_list=['mesroptnamak2@gmail.com',
                                  'mesroptnamak@gmail.com'],
                  from_email=settings.EMAIL_HOST_USER)
        return context


class EmailFormView(FormView):
    template_name = 'email_form.html'
    form_class = EmailForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.GET.get('subject'):
            subject = request.GET.get('subject')
            message = request.GET.get('message')
            message = render_to_string('render_email.html',
                                       {'user': request.user, 'message': message})
            to = request.GET.get('to_email')
            email = EmailMessage(subject=subject, body=message, to=[to])
            email.send()
            return redirect('user_template')
        return render(request, 'email_form.html', {'form': self.get_form()})


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'account/registration.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        email_subject = 'Activate Second Django Account'
        message = render_to_string('account/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = user.email
        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home:home')


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context


class ActivateAccountView(TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            uidb64 = kwargs.get('uidb64')
            token = kwargs.get('token')
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            print(uid)
            user = User.objects.get(pk=uid)
        except Exception as err:
            print(err)
            return HttpResponse('Invalid token or your link expired')
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('home:home')
        return HttpResponse('Invalid token or your link expired')



# class UserDetailView(TemplateView):
#     template_name = 'users/profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # Logic for retrieving the user profile based on the given pk
#         # Replace this with your own logic to fetch the user profile data
#         pk = self.kwargs['pk']
#         user_profile = User.objects.get(pk=pk)
#
#         context['user_profile'] = user_profile
#         return context



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