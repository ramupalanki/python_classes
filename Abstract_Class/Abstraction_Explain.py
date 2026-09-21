from abc import ABC,abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")
class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Processing UPI payment of ${amount}")
class NetBankingPayment(Payment):

    def pay(self, amount):
        print(f"Processing Net Banking payment of ${amount}")

payment1=CreditCardPayment()
payment1.pay(100)

payment2=UPIPayment()
payment2.pay(200)

payment3=NetBankingPayment()
payment3.pay(300)


payment4=Payment()
print("Object created for the abstract class payment")