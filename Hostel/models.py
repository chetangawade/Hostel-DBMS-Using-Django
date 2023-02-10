from django.db import models

# Create your models here.

# for boys
class Boys(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    parent_mobile_no = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

# for girls
class Girls(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    parent_mobile_no = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year = models.CharField(max_length=50)