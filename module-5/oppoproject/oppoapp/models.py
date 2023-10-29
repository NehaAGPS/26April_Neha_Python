from django.db import models
# Create your models here.

class addproduct(models.Model):
 fname=models.CharField(max_length=20)
 lname=models.CharField(max_length=20)
 companyname=models.CharField(max_length=20)
 selection=models.CharField(max_length=20)
 city=models.CharField(max_length=50)
 state=models.CharField(max_length=50)
 postcode=models.BigIntegerField()
 phone=models.BigIntegerField()
 email=models.EmailField()


class productaddreal(models.Model):
   title=models.CharField(max_length=20)
   Price=models.BigIntegerField(max_length=20)
   discription=models.TextField()
   productimage=models.FileField(upload_to='Myfiles')
 
