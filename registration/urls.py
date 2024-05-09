from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import RegistreViews , RegistreViewsAD

urlpatterns = [
    
   
    path('login/', LoginView.as_view() , name ='Login') ,
    path('logout/', LogoutView.as_view() , name ='Logout') ,
    path('registre/', RegistreViews.as_view() , name ='Registre') ,
    path('registreAD/', RegistreViewsAD.as_view() , name ='RegistreAD') ,

    

]