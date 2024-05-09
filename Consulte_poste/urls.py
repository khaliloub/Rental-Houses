from django.urls import path
from .views import HomeView
from .views import MaisonsDetailsViews
from .views import AboutViews
from .views import UserUpdateView 
from .views import AddVillaViews
from .views import AddReservation
from .views import PasswordsViews
from .views import PersonalVillaView
from .views import VillaUpdateView
from .views import ReservationUpdateView
from .views import UserDeleteView
from .views import VillaDeleteView
from .views import ReservationDeleteView , Reservation1DeleteADView , searchbar
from .views import ListeVillaView  , Reservation1UpdateADView
from .views import ListeUserView , AddADReservation , AddADReservation2
from .views import ListeReservationView , AddAppADViews ,ReservationDeleteADView
from .views import HomeAppartView
from .views import AppDetailsViews , AppUpdateADView , AppDeleteADView ,ReservationUpdateADView
from .views import AddReservation2
from .views import AddAppViews , AppUpdateView , PersonalAppView , AppDeleteView , Reservation1DeleteView , Reservation1UpdateView , ListePersReservation1View , ListePersReservation2View ,ListeAppView ,ListeReservation1View ,HomeI , UserADUpdateView , PasswordsADViews , VillaADUpdateView , VillaADDeleteView , AddVillaADDViews

from .import views
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import views as auth_views

app_name ='Consulte_poste'
urlpatterns = [
    path('home0/', HomeI.as_view() , name="homeIn"), 
    path('home/', HomeView.as_view() , name="home"),
    path('home1/', HomeAppartView.as_view() , name="home-Appar"),
    path('details/<int:pk>/', MaisonsDetailsViews.as_view() , name = 'Maison-details') ,
    path('details1/<int:pk>/', AppDetailsViews.as_view() , name = 'App-details') ,
    path('about/', AboutViews.as_view() , name="About-site"),
    path('update/<int:pk>/', UserUpdateView.as_view(), name="Update-user"),
    path('updateUA/<int:pk>/', UserADUpdateView.as_view(), name="Update-userAD"),
    path('addvilla/', AddVillaViews.as_view(), name="Add-villa"),
    path('addvillaAD/', AddVillaADDViews.as_view(), name="Add-villaAD"),
    path('addapp/', AddAppViews.as_view(), name="Add-App"),
    path('addappAD',AddAppADViews.as_view(),name="AddAD-App"),
    path('addreservation/<int:pk>/', AddReservation.as_view() , name="Add-Reservation") ,
    path('addADreservation/', AddADReservation.as_view() , name="Add-ReservationAD") ,
    path('addreservation2/<int:pk>/', AddReservation2.as_view() , name="Add-Reservation2") ,
    path('addADreservation2/', AddADReservation2.as_view() , name="AddAD-Reservation2") ,
    path('password/', PasswordsViews.as_view(template_name='registration/changepassword.html') , name="Pass-change"),
    path('passwordAD/', PasswordsViews.as_view( template_name='registration/changepasswordAD.html') , name="Pass-changeAD"),
    path('listpersonalvilla/',PersonalVillaView.as_view(), name='Liste-Pvilla'),
    path('listpersonalapp/',PersonalAppView.as_view(), name='Liste-PApp'),
    path('updatevilla/<int:pk>/' , VillaUpdateView.as_view(),name='Update-villa'),
    path('updatevillaAD/<int:pk>/' , VillaADUpdateView.as_view(),name='UpdateAD-villa'),
    path('updateapp/<int:pk>/' , AppUpdateView.as_view(),name='Update-App'),
    path('updateADapp/<int:pk>/' , AppUpdateADView.as_view(),name='UpdateAD-App'),
    path('updatereservation/<int:pk>/' , ReservationUpdateView.as_view(),name='Update-reservation' ),
    path('updateADreservation/<int:pk>/' , ReservationUpdateADView.as_view(),name='UpdateAD-reservation' ),
    path('updatereservation1/<int:pk>/' , Reservation1UpdateView.as_view(),name='Update-reservation1' ),
    path('updateADreservation1/<int:pk>/' , Reservation1UpdateADView.as_view(),name='Update-reservationAD1' ),
    path('deleteuser/<int:pk>/', UserDeleteView.as_view(),name="Delete-user"),
    path('deletevilla/<int:pk>/', VillaDeleteView.as_view(),name="Delete-villa"),
    path('deletevillaAD/<int:pk>/', VillaADDeleteView.as_view(),name="DeleteAD-villa"),
    path('deleteapp/<int:pk>/', AppDeleteView.as_view(),name="Delete-App"),
    path('deleteappAD/<int:pk>/', AppDeleteADView.as_view(),name="DeleteAD-App"),
    path('deletereservation/<int:pk>/', ReservationDeleteView.as_view(),name="Delete-reservation"),
    path('deleteADreservation/<int:pk>/', ReservationDeleteADView.as_view(),name="DeleteAD-reservation"),
    path('deletereservation1/<int:pk>/', Reservation1DeleteView.as_view(),name="Delete-reservation1"),
    path('deleteADreservation1/<int:pk>/', Reservation1DeleteADView.as_view(),name="DeleteAD-reservation1"),
    path('listevilla/',ListeVillaView.as_view(),name="Liste-villa"),
    path('listeapp/',ListeAppView.as_view(),name="Liste-app"),
    path('listeuser/',ListeUserView.as_view(),name="Liste-user"),
    path('listereservationvilla/',ListeReservationView.as_view(),name="Liste-ReserVilla"),
    path('listereservationapp/',ListeReservation1View.as_view(),name="Liste-Reserapp"),
    path('listeperreser1/',ListePersReservation1View.as_view(),name="Liste-PersReserVil"),
    path('listeperreser2/',ListePersReservation2View.as_view(),name="Liste-PersReserApp"),
    path('searchbar/',views.searchbar , name='searchbar')

]