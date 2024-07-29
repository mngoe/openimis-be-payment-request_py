class PaymentRequestGQLType(DjangoObjectType):
    """
    Details sur les payments
    """

    class Meta:
        model = PaymentRequest
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "payment_method": ["exact"],
            "phone": ["exact", "icontains"],
            "payment_date": ["exact", "icontains"]
        }
        connection_class = ExtendedConnection