from django.db import models

# Create your models here.


class ContainerDetails(models.Model):
    container_code = models.CharField(max_length=50, null=True, default=None)
    ISO_code = models.CharField(max_length=20, null=True, default=None)
    container_size = models.CharField(max_length=50, null=True, default=None)
    container_type = models.CharField(max_length=500, null=True, default=None)
    gate = models.CharField(max_length=100, null=True, default=None)
    container_owner = models.CharField(max_length=500, null=True, default=None)
    date_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    valid_container = models.BooleanField(default=True)
    image_right = models.TextField(null=True, default=None)
    image_left = models.TextField(null=True, default=None)
    image_rear = models.TextField(null=True, default=None)
    image_top = models.TextField(null=True, default=None)
    

    #def __str__(self):
    #    return self.container_code
