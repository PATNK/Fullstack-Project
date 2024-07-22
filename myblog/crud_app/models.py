from django.db import models

# Create your models here.

class Customer(models.Model):
    gender_choices =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        
    ]

    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40, null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
       return self.name

    