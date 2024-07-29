class PaymentRequest(models.Model):
    id = models.SmallIntegerField(db_column='PaymentId', primary_key=True)
    phone = models.CharField(db_column='Phone', max_length=50)
    payment_method = models.CharField(db_column='PaymentMethod', max_length=50)
    payment_date = models.DateTimeField(db_column="paymentDate", default=django_tz.now, blank=True, null=True)
