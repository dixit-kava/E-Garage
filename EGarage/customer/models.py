
from django.db import models

class contact(models.Model):
    username=models.CharField(max_length=50)
    userphone=models.CharField(max_length=15)
    useremail=models.CharField(max_length=50)
    usercontent=models.TextField()
    def __str__(self):
        return 'message from ' + self.username + ' - ' + self.useremail
    

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name

class Service(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
 
 
	def __str__(self):
         return self.name
    		

     

    	

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('on the way', 'on the way'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Service, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
 
 
    		

	 