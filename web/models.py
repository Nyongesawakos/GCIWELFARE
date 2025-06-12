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
    Firstname = models.CharField(null=True, blank=True, max_length=200)
    name=models.CharField(max_length=255)
    lastName = models.CharField(null=True, blank=True, max_length=200)
    Email = models.EmailField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=200)
    identity= models.IntegerField(null=True, blank=True)
    KANGOYA = 'KANGOYA'  
    KASPHAT = 'KASPHAT'  
    NGARA = 'NGARA'
    GRACE_FAMILY= 'GRACE_FAMILY'
    WHITE_HOUSE = 'WHITE_HOUSE'
    KASARANI= 'KASARANI'
    KIKUYU = 'KIKUYU'
    KENYATTA = 'KENYATTA'
    MUCATHA = 'MUCATHA'
    TRUTH_SEEKERS = 'TRUTH_SEEKERS'
    RUIRU = 'RUIRU'
    GACHIE = 'GACHIE'
    SHAMMAH = 'SHAMMAH'
    THINDIGUA = 'THINDIGUA'
    MOMBASA_RD = 'MOMBASA_RD'
    JAMHURI = 'JAMHURU'
    KAHAWA = 'KAHAWA'
    BLOOM_HILL_KAWAIDA = 'BLOOM_HILL_KAWAIDA'
    THIKA= 'THIKA'

    CHOICES = [
        (KANGOYA,'Kangoya'),
        (KASPHAT,'Kasphat'),
        (NGARA,'Ngara'),
        (GRACE_FAMILY ,'Grace_family'),
        (WHITE_HOUSE,'White_house'),
        (KASARANI,'Kasarani'),
        (KIKUYU ,'Kikuyu'),
        (KENYATTA, 'Kenyatta'),
        (MUCATHA ,'Mucatha'),
        (TRUTH_SEEKERS ,'Truth_seekers'),
        (RUIRU ,'Ruiru'),
        (GACHIE ,'Gachie'),
        (SHAMMAH,'Shammah'),
        (THINDIGUA ,'Thindigua'),
        (MOMBASA_RD,'Mombasa_rd'),
        (JAMHURI,'Jamhuri'),
        (KAHAWA,'Kahawa'),
        (BLOOM_HILL_KAWAIDA,'Bloom_hill_kawaida'),
        (THIKA,'Thika'),
        

    ]
    HBC = models.CharField(null=True, blank=True, max_length=100)  
    choice = models.CharField(  
        max_length=100,  
        choices=CHOICES,  
        default=KANGOYA,  
    )
    #HBC = models.CharField(null=True, blank=True, max_length=200)
   # option1= 'parent'
   # option2= 'child'
    #opition3 ='Spouse'
    #MY_CHOICES =[
        #(option1, 'option 1' ),
        #(option2, 'option 2' ),
        #(option2, 'option 3' ),
   # ]
   # dropdown_field = models.CharField(max_length=20, choices=MY_CHOICES, default=option1) 
    Parent = models.CharField(null=True, blank=True, max_length=200)
    Child = models.CharField(null=True, blank=True, max_length=200)
    Spouse = models.CharField(null=True, blank=True, max_length=200)
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
        room=models.ForeignKey(room,on_delete=models.CASCADE)
        code=models.CharField(max_length=100)
        name=models.CharField(null=True, blank=True, max_length=100)
        amount = models.DecimalField(max_digits=10, decimal_places=1)
        #month = models.CharField(null=True, blank=True, max_length=100)
        JANUARY = 'JAN'  
        FEBRUARY = 'FEB'  
        MARCH = 'MAR'
        APRIL= 'APR'
        MAY = 'MAY'
        JUNE = 'JUNE'
        JULY = 'JULY'
        AUGUST = 'AUG'
        SEPTEMBER = 'SEP'
        OCTOBER = 'OCT'
        NOVEMBER = 'NOV'
        DECEMBER = 'DEC'

        CHOICES = [
        (JANUARY,'January'),
        (FEBRUARY,'February'),
        (MARCH,'March'),
        (APRIL ,'April'),
        (MAY ,'May'),
        (JUNE ,'June'),
        (JULY  ,'July'),
        (AUGUST, 'August'),
        (SEPTEMBER ,'September'),
        (OCTOBER ,'October'),
        (NOVEMBER ,'November'),
        (DECEMBER ,'December'),

    ]
        month = models.CharField(null=True, blank=True, max_length=100)  
        choice = models.CharField(  
        max_length=100,  
        choices=CHOICES,  
        default=JANUARY,  
    )
        updated=models.DateTimeField(auto_now=True)
        created=models.DateTimeField(auto_now_add=True)

        class Meta:
          ordering = ['-updated', '-created']

        def __str__(self):
          return self.choice

class cash_expenditure(models.Model):
    name =models.CharField(max_length=100)
    date =models.DateField(max_length=20)
    Amount=models.DecimalField(max_digits=10, decimal_places=2)
    updated=models.DateTimeField(auto_now=True, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    class Meta:
     ordering = ['-updated', '-created']

    def __str__(self):
      return self.name

        

    

    

   
        




  
    






