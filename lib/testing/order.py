class Order:
    _all = []

    @classmethod
    def all(cls):
        return cls._all

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self._all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Price must be a float")
        if value < 1.0 or value > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value
