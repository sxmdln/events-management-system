from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import ParticipantCreationForm

class ParticipantCreateView(CreateView):
        form_class = ParticipantCreationForm
        template_name= 'signup.html'
        success_url = reverse_lazy('login')


# Create your views here.
