from django.db import models

# Create your models here.
class Contact(models.Model):    # Contant table
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    desc = models.TextField()
    date=models.DateField()
   
    def __str__(self):
        return self.name

class Sell(models.Model):  
    bookname=models.CharField(max_length=122)
    sellername=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    bookprice=models.DecimalField(max_digits=10,decimal_places=2)
    info=models.TextField()
    image=models.ImageField(upload_to='book_images/',blank=True,null=True)
    
    def __str__(self):
        return self.bookname

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)  # Book cover image
    description = models.TextField()
    is_available_for_rent = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

    