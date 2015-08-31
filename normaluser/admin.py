from distutils.command import register
from django.contrib import admin
from normaluser.models import NormalUser, VerificationCode, Board, Post

# Register your models here.

admin.site.register(NormalUser)
admin.site.register(VerificationCode)
admin.site.register(Board)
admin.site.register(Post)