from django.db import models


class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    data = models.JSONField()
