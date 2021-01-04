from django.db import models


class CarSpecs(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return self.car_brand
