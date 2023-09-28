# Generated by Django 4.2.5 on 2023-09-28 07:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Admin'), (2, 'CompanyHR'), (3, 'Staff'), (4, 'Freelancer')], default=1, max_length=10)),
                ('create_type', models.CharField(choices=[(1, 'OWN'), (2, 'Admin')], default=1, max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10)),
                ('alt_mobile_no', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], max_length=1, null=True)),
                ('aadhar_no', models.BigIntegerField()),
                ('clg_sch_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=30)),
                ('field_of_study', models.CharField(max_length=100)),
                ('heighest_qualification', models.CharField(max_length=100)),
                ('passing_year', models.CharField(max_length=20)),
                ('work_experience', models.CharField(max_length=10)),
                ('resume', models.FileField(upload_to='')),
                ('profile_pic', models.FileField(default='avatar.png', upload_to='companyHR/')),
                ('isDelete', models.BooleanField(default=False)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('register_user', models.CharField(choices=[(1, 'Admin'), (2, 'HR'), (3, 'Staff'), (4, 'Freelancer'), (5, 'Referal')], max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_email', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], max_length=1, null=True)),
                ('profile_pic', models.FileField(default='avatar.png', upload_to='staff/')),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=15)),
                ('isDelete', models.BooleanField(default=False)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('freelancer_email', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10)),
                ('unique_user_id', models.CharField(max_length=64, unique=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], max_length=1, null=True)),
                ('profile_pic', models.FileField(default='avatar.png', upload_to='freelancer/')),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=15)),
                ('isDelete', models.BooleanField(default=False)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyHR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hr_email', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], max_length=1, null=True)),
                ('profile_pic', models.FileField(default='avatar.png', upload_to='companyHR/')),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=15)),
                ('isDelete', models.BooleanField(default=False)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=50)),
                ('street_address_line_2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adminPanel.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
