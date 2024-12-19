from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description =models.TextField(max_length=100)
    image =models.ImageField( upload_to="images")
    stock = models.PositiveIntegerField( default = 0)



    def __str__(self):
        return self.name
    
    def 




# class user(models.Model):
#     user = models.CharField( max_length=50)
#     password = models.IntegerField()


# class cart(models.Model):
#     username = models.CharField()
#     item_name = models.CharField( max_length=50)
