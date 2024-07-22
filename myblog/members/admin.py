from django.contrib import admin
from .models import Customer, Employee, Student, Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Employee)
#admin.site.register(Student)
admin.site.register(Product)

class StudentAdmin(admin.ModelAdmin):
    list_display=("Firstname", "Lastname", "Age", "Gender", "Matric_Number", "Class", "Address","EmailAddress")
admin.site.register(Student, StudentAdmin)