from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=225)
    image = models.TextField()
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField()
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.name
