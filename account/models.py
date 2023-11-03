from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=128, blank=False)
    phone = models.CharField(max_length=30, blank=False)
    balance_usd = models.FloatField(default=0)
    balance_rdw = models.FloatField(default=0)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), default='O')
    passport_image = models.ImageField(upload_to='static/passport_images/', null=True, blank=True)
    REQUIRED_FIELDS = ['full_name', 'phone', 'passport_image', "balance_rdw", "balance_usd", "date_of_birth", "gender"]