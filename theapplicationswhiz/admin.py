from django.contrib import admin
from .models import Application, Note, Contact
# Category,

admin.site.register(Application)
admin.site.register(Note)
# admin.site.register(Category)
admin.site.register(Contact)

# Register your models here.
