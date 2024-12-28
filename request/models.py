from django.db import models

from administrator.models import Administrator
from credit_product.models import CreditProduct
from legal_user.models import LegalUser


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    inn_legal_user = models.ForeignKey(LegalUser, on_delete=models.CASCADE)
    credit_product_id = models.ForeignKey(CreditProduct, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=('одобрено', 'обрабатывается', 'отклонено'))
    email_admin = models.ForeignKey(Administrator, on_delete=models.CASCADE)
