from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name + self.last_name

class Commitment(models.Model):
    commitment_date = models.DateField()
    user = models.ForeignKey(User)
    location = models.CharField(max_length=40, blank = True)
    commitment_description = models.CharField(max_length=100, blank = True)
    is_private = models.BooleanField()

    def __str__(self):
        return self.commitment_description