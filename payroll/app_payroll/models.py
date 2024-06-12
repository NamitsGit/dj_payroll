from django.db import models

COUNTRIES = [
    ("IND", "INDIA"),
    ("USA", "United States of America"),
    ("UK", "United Kingdom"),
    ("AUS", "Australia"),
    ("AU", "Austria"),
    ("SP", "Spain"),
]

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title_name = models.CharField(max_length=30)
    has_passport = models.BooleanField()
    salary = models.IntegerField()
    birth_date = models.DateField()
    hire_date = models.DateField()
    notes = models.CharField(max_length=200)
    country = models.CharField(max_length=35, choices=COUNTRIES, default=None)
    email = models.EmailField(default="", max_length=50)
    phone_number = models.CharField(default="", max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
