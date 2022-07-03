from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BloodGroup(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name



class UserDetails(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    contact_no = models.IntegerField()
    req_date = models.DateField()
    blood_group = models.ForeignKey(BloodGroup,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_name)  




class RequestBlood(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    pincode = models.IntegerField()
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    req_date = models.DateTimeField(max_length=100)
 
    def __str__(self):
        return self.name        


