from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    firstname=models.CharField(max_length=255)
    Lastname=models.CharField(max_length=255)
    description =models.TextField(null=True, blank=True)

class tips(models.Model):
    name=models.CharField(max_length=200)  
    description=models.TextField(null=True, blank=True)

class topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name




class room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic=models.ForeignKey(topic, on_delete=models.SET_NULL, null=True) 
    name=models.CharField(max_length=255)
    lastName = models.CharField(null=True, blank=True, max_length=200)
    Email = models.EmailField(null=True, blank=True, max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    identity= models.IntegerField(null=True, blank=True)
    HBC = models.CharField(null=True, blank=True, max_length=200)
   # option1= 'parent'
   # option2= 'child'
    #opition3 ='Spouse'
    #MY_CHOICES =[
        #(option1, 'option 1' ),
        #(option2, 'option 2' ),
        #(option2, 'option 3' ),
   # ]
   # dropdown_field = models.CharField(max_length=20, choices=MY_CHOICES, default=option1) 
    description=models.TextField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    
class message(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE) 
    room=models.ForeignKey(room, on_delete=models.CASCADE) 
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
class update(models.Model):
        owner= models.ForeignKey(User,on_delete=models.CASCADE)
        room=models.ForeignKey(room, on_delete=models.CASCADE)
        code=models.CharField(max_length=100)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        month = models.CharField(null=True, blank=True, max_length=100)
        updated=models.DateTimeField(auto_now=True)
        created=models.DateTimeField(auto_now_add=True)

   
        




  
    






