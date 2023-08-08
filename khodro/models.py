from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.title}'


class Khodro(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=11)
    pelak = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.brand} - {self.model}'