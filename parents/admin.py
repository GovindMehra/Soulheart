from django.contrib import admin
from .models import Chore, Star, Profile

# Register your models here.
admin.site.register(Chore)
admin.site.register(Star)
admin.site.register(Profile)