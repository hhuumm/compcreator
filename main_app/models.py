from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

CHIPS = (('A','AMD'),('I','Intel'))

CARDS=(('A','AMD'),('N','NVIDIA'))

FORMS=(('A','ATX'),('M','MicroATX'))

CERTS=(('0','None'),('b','80 Plus Bronze'),('s','80 Plus Silver'),('g','80 Plus Gold'),('p','80 Plus Platinum'),('t','80 Plus Titanium'))

OS=(('0','No OS'),('w','Windows'),('l','Linux'))

GDDR=(('4','GDDR4'),('5','GDDR5'),('6','GDDR6'))

# Create your models here.
class Chipset(models.Model):
    brand=models.CharField(max_length=1,choices=CHIPS,default=CHIPS[0][0])
    chip_model= models.CharField(max_length=100)
    cores = models.IntegerField()
    threads=models.IntegerField()
    speed = models.DecimalField(max_digits=3,decimal_places=2)
    #Thermal Design Power (Wattage Consumption)
    tdp=models.IntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    link=models.CharField(max_length=200)
    def __str__(self):
        return self.get_brand_display() + " " + self.chip_model 

class Graphics(models.Model):
    brand=models.CharField(max_length=1,choices=CARDS,default=CARDS[0][0])
    graphics_model= models.CharField(max_length=100)
    ram=models.IntegerField()
    ramType=models.CharField(max_length=1,choices=GDDR,default=GDDR[0][0])
    tdp=models.IntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.get_brand_display() + " "+ self.graphics_model

class Case(models.Model):
    name=models.CharField(max_length=100)
    form=models.CharField(max_length=1,choices=FORMS,default=FORMS[0][0])
    price=models.DecimalField(max_digits=8,decimal_places=2)
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ram(models.Model):
    name=models.CharField(max_length=100)
    speed=models.IntegerField()
    amount=models.IntegerField()
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PSU(models.Model):
    name=models.CharField(max_length=100)
    cert=models.CharField(max_length=1,choices=CERTS,default=CERTS[0][0])
    wattage=models.IntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class OS(models.Model):
    name=models.CharField(max_length=1,choices=OS,default=OS[0][0])
    price=models.DecimalField(max_digits=8,decimal_places=2)
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.get_name_display()

class MotherBoard(models.Model):
    name=models.CharField(max_length=100)
    form=models.CharField(max_length=1,choices=FORMS,default=FORMS[0][0])
    socket=models.CharField(max_length=1,choices=CHIPS,default=CHIPS[0][0])
    price=models.DecimalField(max_digits=8,decimal_places=2)
    link=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class CustomComputer(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    mobo=models.ForeignKey(MotherBoard,on_delete=models.RESTRICT,blank=True, null=True)
    psu=models.ForeignKey(PSU,on_delete=models.RESTRICT,blank=True, null=True)
    os = models.ForeignKey(OS,on_delete=models.RESTRICT,blank=True, null=True)
    ram=models.ForeignKey(Ram,on_delete=models.RESTRICT,blank=True, null=True)
    case=models.ForeignKey(Case,on_delete=models.RESTRICT,blank=True, null=True)
    gpu=models.ForeignKey(Graphics,on_delete=models.RESTRICT,blank=True, null=True)
    cpu = models.ForeignKey(Chipset,on_delete=models.RESTRICT,blank=True, null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2,blank=True, null=True)
    def __str__(self):
        return self.name

    




   


