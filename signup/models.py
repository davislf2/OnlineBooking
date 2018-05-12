from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birth_date = models.DateField(null=True, blank=True)
#     address_1 = models.CharField(max_length=128)
#     address_2 = models.CharField(max_length=128, blank=True)
#
#     city = models.CharField(max_length=64, default="Zanesville")
#     state = models.CharField(max_length=3, default="VIC")
#     zip_code = models.CharField(max_length=4, default="3103")
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=100, null=True)
    full_name = models.TextField(max_length=30, null=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
