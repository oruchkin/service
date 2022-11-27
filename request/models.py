from django.db import models

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length=50)


class Request(models.Model):
    room = models.ForeignKey("request.Room", verbose_name="комната", on_delete=models.CASCADE)
    created = models.DateTimeField('created',auto_now_add=True)
    json_data = models.JSONField("json_data", blank=True, null=True)
    headers = models.JSONField("headers", blank=True, null=True)