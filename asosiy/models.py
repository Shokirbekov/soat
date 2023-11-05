from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    J = [
        ("Male", "Male"),
        ("Female", "Female")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    when_created = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=J)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Watch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='watch_images/', null=True, blank=True)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class BuyList(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.watch.name}, {self.profil.name}"
