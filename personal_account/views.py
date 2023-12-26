<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CastomUserCreationForm

class UserCreateView(CreateView):
    model = CastomUser
    form_class = CastomUserCreationForm
    success_url = reverse_lazy('profile')
    template_name = 'profile/register.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.first_name =form.cleaned_data['first_name']
        user.birth_date =form.cleaned_data['birth_date']
        user.save()
        login(self.request, user)
        return super().form_valid(form)




class ProfileView(TemplateView):
    template_name = 'profile/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
>>>>>>> develop
