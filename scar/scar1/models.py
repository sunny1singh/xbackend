from django.db import models

# Create your models here.
class allcommon(models.Model):
    image = models.ImageField(upload_to='images')
    name=models.CharField(max_length=64)
    price=models.IntegerField()
    off=models.IntegerField()
    class Meta:
        abstract=True

class DairyItems(allcommon):
    pass

class Babycare(allcommon):
    pass

class Fruits(allcommon):
    pass

class snacks(allcommon):
    pass

class Vegetables(allcommon):
    pass