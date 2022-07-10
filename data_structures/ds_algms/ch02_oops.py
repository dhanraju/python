"""OOPS concepts."""

class CreditCard:
  """A consumer credit card."""

  def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.""

    The initial balance is zero.


    Args:
      customer(string): The name of the customer
      bank(string): The name of the bank
      acnt(string): The account identifier
      limit(float): Credit limit (measured in dollars)
    """
    self._customer = customer
    # Identifiers that begin with a single leading underscore are intended to
    # suggest that they are only for "internal" use to a class or module, and
    # not part of a public interface. This is called "Encapsulation".
    # "self" is an identifier that identifies the instance upon which a method
    # is invoked.
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Returns name of the customer."""
    return self._customer

  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Retun current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if (price + self._balance) > self._limit:
      return False
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balances."""
    self._balance -= amount


def main():
    my_card = CreditCard('John Bowman', 'California Savings',
                         '5391 0375 9387 5309', 2500)
    print("*** Customer name = %s ***" % my_card.get_customer())


if __name__ == '__main__':
    main()