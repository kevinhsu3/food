from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# One profile is associated with one user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Need to delete Profile for the user to be deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'
