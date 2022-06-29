from django.contrib import admin
from .models import My_List, Country, Contacts


admin.site.register(Contacts)
admin.site.register(My_List)
admin.site.register(Country)
