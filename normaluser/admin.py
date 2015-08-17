from distutils.command import register
from django.contrib import admin
from normaluser.models import NormalUser, VerificationCode

# Register your models here.

admin.site.register(NormalUser)
admin.site.register(VerificationCode)