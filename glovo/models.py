from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name







