import pytest
from coffee import Coffee
from customer import Customer


def test_coffee_orders():
    coffee = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 4.0)
    assert len(coffee.orders()) == 2

def test_coffee_customers():
    coffee = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 4.0)
    assert len(coffee.customers()) == 2
