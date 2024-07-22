from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.user.username

# Create your models here.
#A customer model which represents the customer table in the data base.
class Customer(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)

#Creating an Employee model with the following attributes: employee name, designation, date of joining, age and gender
class Employee(models.Model):
    Firstname = models.CharField(max_length=35)
    Designation = models.CharField(max_length=35)
    Employment_date = models.CharField(max_length=35)
    Age = models.CharField(max_length=35)
    Gender = models.CharField(max_length=35)
    Next_of_Kin = models.CharField(max_length=35, null=True)
    Salary = models.CharField(max_length=35, null=True)

    #Creating a Student Model (or Table) with the following attrinbutes:  names(first and last), age, gender, matric no., class and address
class Student(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Age=models.CharField(max_length=30)
    Gender=models.CharField(max_length=30)
    Matric_Number=models.CharField(max_length=30)
    Class=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    EmailAddress=models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"

    #Creating a Product Model/Table with the following attributes: Product name, price, quantity, expiry date.
class Product(models.Model):
    Productname=models.CharField(max_length=35)
    Price=models.CharField(max_length=35)
    Quantity=models.CharField(max_length=35)
    Expirydate=models.CharField(max_length=35)

    def __str__(self):
        return f"{self.Productname}"