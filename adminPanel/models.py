from django.contrib.auth.models import AbstractUser # Use to create customuser.
from django.db import models
from django.dispatch import receiver # Use to create receiver to a signals.
from django.db.models.signals import post_save # Use to save signals.



# For user type.
class CustomUser(AbstractUser):
    user_type_data = ((1,'Admin'),(2,'CompanyHR'), (3,'Staff'), (4, 'Freelancer'))
    create_type_data = ((1, 'OWN'),(2, 'Admin'))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    create_type = models.CharField(default=1, choices=create_type_data, max_length=10)
    isDelete = models.BooleanField(default=False)


# For Admin.
class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# For CompanyHR.
class CompanyHR(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    hr_email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField(default='avatar.png', upload_to='companyHR/')
    address = models.TextField()
    password = models.CharField(max_length=15)
    isDelete = models.BooleanField(default=False)
    birth_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# For Staffs.
class Staffs(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    staff_email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField(default='avatar.png', upload_to='staff/')
    address = models.TextField()
    password = models.CharField(max_length=15)
    isDelete = models.BooleanField(default=False)
    birth_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# For Freelancer.
class Freelancer(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    freelancer_email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    unique_user_id = models.CharField(max_length=64, unique=True)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    profile_pic = models.FileField(default='avatar.png', upload_to='freelancer/')
    address = models.TextField()
    password = models.CharField(max_length=15)
    isDelete = models.BooleanField(default=False)
    birth_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# For Candidates.
class Candidate(models.Model):
    GENDER = (
        ('M', 'M'), # Male
        ('F', 'F'), # Female
        ('O', 'O'), # Other
    )
    CREATE_TYPE = (
        (1, 'Admin'), # Admin
        (2, 'HR'), # HR
        (3, 'Staff'), # Staff
        (4, 'Freelancer'), # Freelancer
        (5, 'Referal') # In referal link
    )
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    alt_mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    aadhar_no = models.BigIntegerField()
    clg_sch_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=30)
    field_of_study = models.CharField(max_length=100)
    heighest_qualification = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=20)
    work_experience = models.CharField(max_length=10)
    resume = models.FileField()
    profile_pic = models.FileField(default='avatar.png', upload_to='companyHR/')
    isDelete = models.BooleanField(default=False)
    birth_date = models.DateTimeField(null=True, blank=True)
    register_user = models.CharField(max_length=10, null=True, choices=CREATE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()    


# For Candidate address.
class CandidateAddress(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=50)
    street_address_line_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# This for create user type account automatically.
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            CompanyHR.objects.create(
                admin=instance,
                hr_email="",
                address="",
                mobile_no="",
                profile_pic="",
                gender="",
                password=""
            )
        if instance.user_type==3:
            Staffs.objects.create(
                admin=instance,
                staff_email="",
                address="",
                mobile_no="",
                profile_pic="",
                gender="",
                password=""
            )
        if instance.user_type==4:
            Freelancer.objects.create(
                admin=instance,
                freelancer_email="",
                address="",
                mobile_no="",
                profile_pic="",
                gender="",
                password=""
            )


# This for save create user type account automatically.
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.companyhr.save()
    if instance.user_type==3:
        instance.staff.save()
    if instance.user_type==4:
        instance.freelancer.save()