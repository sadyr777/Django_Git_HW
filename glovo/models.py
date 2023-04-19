from django.db import models



class Courier(models.Model):
    fullname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname
        
      
class Order(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
