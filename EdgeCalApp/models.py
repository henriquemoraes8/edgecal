from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class Commitment(models.Model):
    commitment_date = models.DateField()
    user = models.ForeignKey(User)
    is_private = models.BooleanField()