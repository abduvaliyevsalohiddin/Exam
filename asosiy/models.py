from django.db import models
from django.contrib.auth.models import User


class Suv(models.Model):
    brend = models.CharField(max_length=30)
    narx = models.PositiveSmallIntegerField()
    litr = models.PositiveSmallIntegerField()
    batafsil = models.TextField()

    def __str__(self):
        return self.brend


class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=50)
    qarz = models.PositiveSmallIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Admin(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    ish_vaqti = models.CharField(max_length=5)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Haydovchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    kiritilgan_sana = models.DateField()

    def __str__(self):
        return self.ism


class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    umumiy_narx = models.PositiveIntegerField(default=0)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
