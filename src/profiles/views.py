from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy



# Create your views here.
class SignInView(LoginView):
    template_name = 'profiles/signin.html'


class RegisterUserView(FormView):
    form_class = UserCreationForm
    template_name = 'profiles/register.html'
    success_url = reverse_lazy('profiles:signin')
    success_message = 'Basari ile kayit oldunuz, Giris yapiniz!'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
