from django.db import models

class Administrator(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    login = models.CharField(max_length=50)
