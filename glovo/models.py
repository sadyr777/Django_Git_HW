from django.db import models


class Courier(models.Model):
    fullname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname
