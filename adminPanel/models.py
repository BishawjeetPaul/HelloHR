from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUser(AbstractUser):
    user_type_data = ((1, 'ADMIN'), (2, 'StaffHR'), (3, 'Freelancer'), (4, 'ConpanyHR'))
    user_type = models.CharField(default=1, choices=user_type_data,  max_length=10)
    isDelete = models.BooleanField(default=False)


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StaffHR(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField()
    address = models.TextField()
    isDelete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



class Freelancer(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField()
    address = models.TextField()
    isDelete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class CompanyHR(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField()
    address = models.TextField()
    isDelete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()