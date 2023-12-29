from django.db import models

# Create your models here.

class UserDetails(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    mobilenumber = models.CharField(max_length=15)
    organization = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    