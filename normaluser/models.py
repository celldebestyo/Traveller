from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class NormalUser(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=10, default='Male')
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True, default=datetime.datetime.now)
    age = models.IntegerField(default=0)
    followings = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='following')
    followers = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='follower')
    phoneNumber = models.CharField(max_length=30, null=True, blank=True)
    postalCode = models.CharField(max_length=30, null=True, blank=True)
    IdentityNumber = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.email

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    date = models.DateField(default=datetime.datetime.now);
    likeCount = models.IntegerField(default=0)
    sharedCount = models.IntegerField(default=0)
    author = models.ForeignKey(NormalUser, related_name='author')
    owner = models.ForeignKey(NormalUser, related_name='owner')
    relatedAs = models.CharField(max_length=255)

class Calendar(models.Model):
    user = models.ForeignKey(NormalUser)

class Board(models.Model):
    admin = models.ForeignKey(NormalUser, related_name='admin')
    name = models.CharField(max_length=255)
    description = models.TextField()
    participants = models.ManyToManyField(NormalUser, related_name='participants')
    followers = models.ManyToManyField(NormalUser, related_name='board_followers')


class Event(models.Model):
    calendar = models.ForeignKey(Calendar)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    invitees = models.ManyToManyField(NormalUser)

class VerificationCode(models.Model):
    user = models.OneToOneField(User)
    code = models.CharField(max_length=12)

    def __str__(self):
        return self.user.email + ": " + self.code
