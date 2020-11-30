#Django
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Forms
from .forms import *


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/login/'


class LoginView(SuccessMessageMixin, LoginView):
    template_name="login.html"
    success_message = "Bienvenido %(first_name)s %(last_name)s!"

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name=self.request.user.first_name.capitalize(),
            last_name=self.request.user.last_name.capitalize(),
        )


class SignUpView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registerform.html'
    success_url = '/login/'
    success_message = "Usuario creado exitosamente"