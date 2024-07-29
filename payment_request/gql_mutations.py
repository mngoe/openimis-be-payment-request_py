class SendPaytRequestMutation(OpenIMISMutation):
	@classmethod
    def async_mutate(cls, user, **data):
        try:
            payment_request = data.get('payment_request')
            if payment_request:
                payment_request.send_request()
            return None
        except Exception as exc:
            logger.exception("payment_request.mutation.failed_to_send_request")
            return [{
                'message': _("payment_request.mutation.failed_to_send_request"),
                'detail': str(exc)}
            ]
