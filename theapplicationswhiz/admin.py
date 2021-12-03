from django.contrib import admin
from .models import Application, Note, Category

admin.site.register(Application)
admin.site.register(Note)
admin.site.register(Category)

# Register your models here.
