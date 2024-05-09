#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render
from django.views.generic import View , TemplateView , ListView , DetailView , FormView , UpdateView 
from django.contrib.auth.forms import UserChangeForm  
#from django.http import HttpResponse
from .models import Villa 
from .models import ResrvationVilla
from .models import ResrvationAppartement
from .models import Appartement
from django.contrib.auth.models import User 
from django.views.generic.edit import CreateView 
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordChangeView 








class HomeI(TemplateView):
    template_name = 'Home0.html'


class HomeView(ListView):
    template_name = 'Home.html'
    model = Villa

class HomeAppartView(ListView):
    template_name = 'HomeAppart.html'
    model = Appartement

class PersonalVillaView(ListView):
    template_name = 'PersVillaList.html'
    model = Villa

class PersonalAppView(ListView):
    template_name = 'PersappList.html'
    model = Appartement

class ListeVillaView(ListView):
    template_name = 'listeVillaList.html'
    model = Villa
    context_object_name = 'a'

class ListeAppView(ListView):
    template_name = 'listeAppList.html'
    model = Appartement
    context_object_name = 'a'

class ListeUserView(ListView):
    template_name = 'listeUser.html'
    model = User
    context_object_name = 'a'

class ListeReservationView(ListView):
    template_name = 'listeReservation.html'
    model = ResrvationVilla
    context_object_name = 'a'



class ListeReservation1View(ListView):
    template_name = 'listeReservation1.html'
    model = ResrvationAppartement
    context_object_name = 'a'


class ListePersReservation1View(ListView):
    template_name = 'listePersReservation1.html'
    model = ResrvationVilla
    context_object_name = 'a'

class ListePersReservation2View(ListView):
    template_name = 'listePersReservation2.html'
    model = ResrvationAppartement
    context_object_name = 'a'
  


class MaisonsDetailsViews(DetailView):
    template_name = 'Details.html'
    model = Villa 
    context_object_name = 'a'

class AppDetailsViews(DetailView):
    template_name = 'DetailsApp.html'
    model = Appartement 
    context_object_name = 'a'





class AboutViews(TemplateView):
    template_name = 'About.html'


class UserUpdateView(UpdateView):
    template_name='UpdateUser.html'
    model = User
    fields = ["username"]
    success_url = '/home0/' 

class UserADUpdateView(UpdateView):
    template_name='UpdateUserAd.html'
    model = User
    fields = ["username"]
    success_url = '/listeuser/'

class UserDeleteView(DeleteView):
    template_name='deleteuser.html'
    model=User
    success_url = '/listeuser/'

class VillaUpdateView(UpdateView):
    template_name="Updatevilla.html"
    model=Villa
    fields=["Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumVilla","Piscine"]
    success_url='/listpersonalvilla/'

class VillaADUpdateView(UpdateView):
    template_name="UpdatevillaAD.html"
    model=Villa
    fields=["Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumVilla","Piscine"]
    success_url='/listevilla/'


class AppUpdateView(UpdateView):
    template_name="Updateapp.html"
    model=Appartement
    fields=["Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumImmeble","NumEtage","NumAppartement"]
    success_url='/listpersonalapp/'

class AppUpdateADView(UpdateView):
    template_name="UpdateADapp.html"
    model=Appartement
    fields=["Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumImmeble","NumEtage","NumAppartement"]
    success_url='/listeapp/'

class VillaDeleteView(DeleteView):
    template_name='deletevilla.html'
    model=Villa
    context_object_name = 'a'
    success_url = '/listpersonalvilla/'


class VillaADDeleteView(DeleteView):
    template_name='deletevillaAD.html'
    model=Villa
    context_object_name = 'a'
    success_url = '/listevilla/'

class AppDeleteView(DeleteView):
    template_name='deleteapp.html'
    model=Appartement
    context_object_name = 'a'
    success_url = '/listpersonalapp/'

class AppDeleteADView(DeleteView):
    template_name='deleteappAD.html'
    model=Appartement
    context_object_name = 'a'
    success_url = '/listeapp/'

class ReservationUpdateView(UpdateView):
    template_name="Updatereservation.html"
    model=ResrvationVilla
    fields = ["house","StartDayReser","EndDayReser"]
    success_url='/listeperreser1/'

class ReservationUpdateADView(UpdateView):
    template_name="UpdatereservationAD.html"
    model=ResrvationVilla
    fields = ["user","house","StartDayReser","EndDayReser"]
    success_url='/listereservationvilla/'

class Reservation1UpdateView(UpdateView):
    template_name="Updatereservation1.html"
    model=ResrvationAppartement
    fields = ["house","StartDayReser","EndDayReser"]
    success_url='/listeperreser2/'

class Reservation1UpdateADView(UpdateView):
    template_name="UpdatereservationAD1.html"
    model=ResrvationAppartement
    fields = ["user","house","StartDayReser","EndDayReser"]
    success_url='/listereservationapp/'

class ReservationDeleteView(DeleteView):
    template_name='deletereservation.html'
    model=ResrvationVilla
    context_object_name = 'a'
    success_url = '/listeperreser1/'

class ReservationDeleteADView(DeleteView):
    template_name='deleterADeservation.html'
    model=ResrvationVilla
    context_object_name = 'a'
    success_url = '/listereservationvilla/'

class Reservation1DeleteView(DeleteView):
    template_name='deletereservation1.html'
    model=ResrvationAppartement
    context_object_name = 'a'
    success_url = '/listeperreser2/'

class Reservation1DeleteADView(DeleteView):
    template_name='deleteADreservation1.html'
    model=ResrvationAppartement
    context_object_name = 'a'
    success_url = '/listereservationapp/'

class PasswordsViews(PasswordChangeView):
    success_url = '/home0/'

class PasswordsADViews(PasswordChangeView):
   
    success_url = '/listeuser/'

class AddVillaViews(CreateView):
    template_name = 'AddVilla.html'
    model = Villa
    fields = ["Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumVilla","Piscine"]
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AddVillaADDViews(CreateView):
    template_name = 'AddVillaAD.html'
    model = Villa
    fields = ["user","Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumVilla","Piscine"]
    success_url = '/listevilla/'
    

class AddAppViews(CreateView):
    template_name = 'AddApp.html'
    model = Appartement
    fields = ["Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumImmeble","NumEtage","NumAppartement"]
    success_url = '/home1/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddAppADViews(CreateView):
    template_name = 'AddAppAD.html'
    model = Appartement
    fields = ["user","Title","Description","Address","StartDay","EndDay","Image1","Image2","Image3","Image4","PrixDay","NumImmeble","NumEtage","NumAppartement"]
    success_url = '/listeapp/'

class AddReservation(LoginRequiredMixin ,CreateView ):
    template_name = 'AddReservation.html'
    model = ResrvationVilla
    fields = ["house","StartDayReser","EndDayReser"]
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AddADReservation(CreateView ):
    template_name = 'AddADReservation.html'
    model = ResrvationVilla
    fields = ["user","house","StartDayReser","EndDayReser"]
    success_url = '/listereservationvilla/'
    

class AddReservation2(LoginRequiredMixin ,CreateView ):
    template_name = 'AddReservation2.html'
    model = ResrvationAppartement
    fields = ["house","StartDayReser","EndDayReser"]
    success_url = '/home1/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class AddADReservation2(LoginRequiredMixin ,CreateView ):
    template_name = 'AddReservationAD2.html'
    model = ResrvationAppartement
    fields = ["user","house","StartDayReser","EndDayReser"]
    success_url = '/listereservationapp/'
    
    

def searchbar(request):
    if request.method =='GET':
        search= request.GET.get('search')
        v=Villa.objects.all().filter(title=search)
        return render(request,'searchbar.html',{'v':v})

    

