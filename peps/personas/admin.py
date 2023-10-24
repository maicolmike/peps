from django.contrib import admin

# Register your models here.
from .models import PersonaPEP, Familiar


admin.site.register(PersonaPEP)
admin.site.register(Familiar)