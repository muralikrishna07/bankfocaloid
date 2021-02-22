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



class accounInfoModel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    accountNumber = models.CharField(max_length=100,unique=True)
    mpin = models.IntegerField(unique=True)
    balace = models.IntegerField(default=1000)

    def __str__(self):
        return self.mpin

    def get_absolute_url(self):
        return reverse('success', kwargs={'slug':self.slug})

class Transferdetails(models.Model):
    mpin=models.IntegerField(max_length=6)
    accountnumber=models.CharField(max_length=15)
    amount=models.IntegerField()

    def __str__(self):
        return self.mpin+ self.accountnumber