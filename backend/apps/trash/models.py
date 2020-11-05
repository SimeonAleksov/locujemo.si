from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_description = models.CharField
    recycle_group_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_created=True)


class RecycleGroup(models.Model):
    group_name = models.CharField(max_length=256)
    group_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_created=True)
