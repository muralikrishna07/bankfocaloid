from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class createprofilemodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    address = models.TextField(max_length=200)
    
    date_of_birth = models.DateField(max_length=100)
    phnonenumber = models.IntegerField(unique=True)

    def __str__(self):
        return self.phnonenumber 