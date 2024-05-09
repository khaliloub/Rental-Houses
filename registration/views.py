from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.views.generic import CreateView

# Create your views here.

class RegistreViews(CreateView):
    template_name = 'registration/registrer.html'
    model = User
    form_class = UserCreationForm
    success_url = '/login/'

class RegistreViewsAD(CreateView):
    template_name = 'registration/registreAD.html'
    model = User
    form_class = UserCreationForm
    success_url = '/listeuser/'