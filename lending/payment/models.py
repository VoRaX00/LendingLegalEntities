from django.db import models

from lending.legal_user.models import LegalUser


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    inn_legal_user = models.ForeignKey(LegalUser, on_delete=models.CASCADE)
    recommended_payment = models.IntegerField()
    delay = models.IntegerField(default=0)
    date_payment = models.DateField()
    date_replenishment = models.DateField()