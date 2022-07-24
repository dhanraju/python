"""Extension of credit card using inheritance concept."""
from data_structures.ds_algms.ch02_oops_credit_card import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        Args:
          customer(string): The name of the customer
          bank(string): The name of the bank
          acnt(string): The account identifier
          limit(string): The credit limit
          apr(string): Annual percentage rate
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
          price(int): Charge given price to the card.

        Returns:
          success(bool): True if charge was processed and False if it is denied.
        """
        success = super().charge(price)
        print(success)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


def main():
    my_card = PredatoryCreditCard('John Bowman', 'California Savings',
                                  '5391 0375 9387 5309', 2500, 5)
    print("*** Customer name = %s ***" % my_card.get_customer())
    print("*** Bank name = %s ***" % my_card.get_bank())



if __name__ == '__main__':
    main()