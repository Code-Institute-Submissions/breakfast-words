from django.db import models

# Code to prevent the VSM from generating warning, eg, class 'home' has no
# objects member'. From StackOverflow
# https://stackoverflow.com/questions/45135263/class-has-no-objects-member
# response by buuencrypted 17 July 2017
objects = models.Manager()

# Create your models here.
