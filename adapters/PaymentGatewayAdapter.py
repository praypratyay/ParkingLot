from abc import ABC, abstractmethod

class PaymentGatewayAdapter:

    @abstractmethod
    def pay():
        pass