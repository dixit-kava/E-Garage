from django.db import models

# Create your models here.
class Garage(models.Model):
    garagename=models.CharField(max_length=50)
    ownername=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return 'garage name is ' + self.garagename + ' and owner is  ' + self.ownername
    
    
class Service(models.Model):
    fk = models.ForeignKey(Garage,null=True, on_delete=models.CASCADE)
    gname = models.CharField(max_length=30)
    services = models.CharField(max_length=1000)
    