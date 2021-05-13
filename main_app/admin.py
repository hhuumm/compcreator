from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Chipset)
admin.site.register(OS)
admin.site.register(MotherBoard)
admin.site.register(Case)
admin.site.register(Graphics)
admin.site.register(PSU)
admin.site.register(CustomComputer)
admin.site.register(Ram)


