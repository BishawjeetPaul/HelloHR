from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save




class CustomUser(AbstractUser):
    user_type_data = ((1,'Admin'),(2,'Staff'), (3,'Freelancer'), (4, 'CompanyHR'))
    create_type_data = ((1, 'OWN'),(2, 'Admin'))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    create_type = models.CharField(default=1, choices=create_type_data, max_length=10)
    isDelete = models.BooleanField(default=False)



class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



class Staffs(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField(default='avatar.png', upload_to='avatars/staff/')
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
    profile_pic = models.FileField(default='avatar.png', upload_to='avatars/staff/')
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
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField(default='avatar.png', upload_to='avatars/staff/')
    address = models.TextField()
    isDelete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staffs.objects.create(
                admin=instance,
                address="",
                mobile_no="",
                profile_pic="",
                gender=""
            )
        if instance.user_type==3:
            Freelancer.objects.create(
                admin=instance,
                address="",
                mobile_no="",
                profile_pic="",
                gender=""
            )
        if instance.user_type==4:
            CompanyHR.objects.create(
                admin=instance,
                address="",
                mobile_no="",
                profile_pic="",
                gender=""
            )

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staffs.save()
    if instance.user_type==3:
        instance.freelancer.save()
    if instance.user_type==4:
        instance.companyhr.save()