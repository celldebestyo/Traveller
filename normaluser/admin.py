from distutils.command import register
from django.contrib import admin
from normaluser.models import NormalUser

# Register your models here.

admin.site.register(NormalUser)