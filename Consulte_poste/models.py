
from django.db import models
from django.conf import settings
from datetime import date , datetime , timedelta , timezone 
import datetime
from django.core.exceptions import ValidationError



# Create your models here.
class Maison(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Title = models.CharField(max_length=20) 
    Description = models.CharField(max_length=100)
    Address =models.CharField(max_length=40)
    Image1 = models.ImageField()
    Image2 = models.ImageField()
    Image3 = models.ImageField()
    Image4 = models.ImageField()
    PrixDay = models.PositiveIntegerField()
    StartDay =models.DateField() 
    EndDay = models.DateField() 

    def __str__(self):
        return self.Title
    
    
    def clean(self, *args, **kwargs):
        super(Maison, self).clean(*args, **kwargs)
        if self.StartDay < date.today() :
            raise ValidationError('Start time must be later than now.')
        if self.EndDay <= self.StartDay :
            raise ValidationError('End time must be later than Start time.')
        


        
    
    class Meta :
        abstract = True

class Appartement(Maison):
    
    NumImmeble = models.PositiveIntegerField()
    NumEtage= models.PositiveIntegerField()
    NumAppartement=models.PositiveIntegerField()



class Villa(Maison):
    
    NumVilla=models.PositiveIntegerField()
    Piscine = models.BooleanField()


class MaisonComplet(Maison):
    
    NumMaiCom=models.PositiveIntegerField()
    NombreEtages =models.PositiveIntegerField()
    ToitTerrasse = models.BooleanField()

class ResrvationVilla(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(Villa, on_delete=models.CASCADE)
    StartDayReser =models.DateField()
    EndDayReser =models.DateField() 



    

    def clean(self, *args, **kwargs):
        super(ResrvationVilla, self).clean(*args, **kwargs)
        if self.StartDayReser < self.house.StartDay or self.StartDayReser > self.house.EndDay :
            raise ValidationError('Invalide date.')
        if self.EndDayReser > self.house.EndDay or self.EndDayReser < self.StartDayReser :
            raise ValidationError('Invalide date.')
        if check_availability(self.house , self.StartDayReser , self.EndDayReser)==False:
            raise ValidationError('Invalide date.')




        
    def __str__(self):
        return self.house.Title
    


class ResrvationAppartement(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(Appartement, on_delete=models.CASCADE)
    StartDayReser =models.DateField()
    EndDayReser =models.DateField() 



    

    def clean(self, *args, **kwargs):
        super(ResrvationAppartement, self).clean(*args, **kwargs)
        if self.StartDayReser < self.house.StartDay or self.StartDayReser > self.house.EndDay :
            raise ValidationError('Invalide date.')
        if self.EndDayReser > self.house.EndDay or self.EndDayReser < self.StartDayReser :
            raise ValidationError('Invalide date.')
        if check_availability1(self.house , self.StartDayReser , self.EndDayReser)==False:
            raise ValidationError('Invalide date.')




        
    def __str__(self):
        return self.house.Title
    



class ResrvationMaisonComplet(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(MaisonComplet, on_delete=models.CASCADE)
    StartDayReser =models.DateField()
    EndDayReser =models.DateField() 



    

    def clean(self, *args, **kwargs):
        super(ResrvationMaisonComplet, self).clean(*args, **kwargs)
        if self.StartDayReser < self.house.StartDay :
            raise ValidationError('Start time non disponible.')
        if self.EndDayReser > self.house.EndDay :
            raise ValidationError('End time non disponible.')
        if check_availability2(self.house , self.StartDayReser , self.EndDayReser)==False:
            raise ValidationError('Deja')




        
    def __str__(self):
        return self.house.Title
        

def check_availability(villa , iin , ouut):
    avail_list=[]
    reservation_liste= ResrvationVilla.objects.filter(house=villa)
    for reservation in reservation_liste:
        if reservation.StartDayReser > ouut or reservation.EndDayReser < iin:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

def check_availability1(villa , iin , ouut):
    avail_list=[]
    reservation_liste= ResrvationAppartement.objects.filter(house=villa)
    for reservation in reservation_liste:
        if reservation.StartDayReser > ouut or reservation.EndDayReser < iin:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

def check_availability2(villa , iin , ouut):
    avail_list=[]
    reservation_liste= ResrvationMaisonComplet.objects.filter(house=villa)
    for reservation in reservation_liste:
        if reservation.StartDayReser > ouut or reservation.EndDayReser < iin:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)




