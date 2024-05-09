from django.contrib import admin
from .models import Maison
from .models import MaisonComplet
from .models import Appartement
from .models import Villa
from .models import ResrvationVilla
from .models import ResrvationAppartement
from .models import ResrvationMaisonComplet

# Register your models here.

class MaisonAdmin(admin.ModelAdmin):
    pass

admin.site.register(MaisonComplet, MaisonAdmin)
admin.site.register(Appartement, MaisonAdmin)
admin.site.register(Villa, MaisonAdmin)

admin.site.register(ResrvationVilla)
admin.site.register(ResrvationAppartement)
admin.site.register(ResrvationMaisonComplet)

