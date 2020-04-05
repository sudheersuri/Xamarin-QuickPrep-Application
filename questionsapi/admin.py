from django.contrib import admin
from .models import Questions,subjects
# Register your models here.

admin.site.register(subjects)
admin.site.register(Questions)