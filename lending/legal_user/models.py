from django.db import models

class LegalUser(models.Model):
    inn = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    type_activity = models.CharField(unique=True, max_length=50)
    contact_person = models.CharField()
    address = models.CharField()
