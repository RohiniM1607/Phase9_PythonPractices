from typing import Protocol


class PaymentMethod(Protocol):

    def authorize_payment(self, amount: float) -> bool:
        pass

    def process_payment(self, amount: float) -> bool:
        pass


class CreditCardPayment:

    def authorize_payment(self, amount: float) -> bool:
        print(f"Authorizing credit card payment of ${amount}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        return True


class PayPalPayment:

    def authorize_pament(self, amount: float) -> bool:
        print(f"Authorizing PayPal payment of ${amount}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True


def process_order(payment: PaymentMethod, amount: float):

    if payment.authorize_payment(amount):
        payment.process_payment(amount)
        print("Payment successful")

    else:
        print("Payment authorization failed")


credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

process_order(credit_card_payment, 100)
process_order(paypal_payment, 200)