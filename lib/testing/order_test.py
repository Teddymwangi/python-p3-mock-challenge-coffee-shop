import pytest
from order import Order
from coffee import Coffee
from customer import Customer


def test_order_init():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_customer_type():
    with pytest.raises(ValueError):
        Order("InvalidCustomer", Coffee("Latte"), 5.0)
