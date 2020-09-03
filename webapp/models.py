from django.db import models

# Create your models here.
class userInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    porfile_picture = models.ImageField()
    email = models.CharField(max_length=100)
    dob = models.DateField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name