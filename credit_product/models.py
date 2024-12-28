from django.db import models

class CreditProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type_product = models.CharField(max_length=50)
    percent = models.FloatField()
    repayment_period = models.IntegerField()
    amount = models.FloatField()
    recommended_payment = models.FloatField()


