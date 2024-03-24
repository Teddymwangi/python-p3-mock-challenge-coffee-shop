import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_customer_init():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_change():
    customer = Customer("Alice")
    customer.name = "Bob"
    assert customer.name == "Bob"

def test_customer_invalid_name_type():
    with pytest.raises(ValueError):
        Customer(123)

def test_customer_invalid_name_length():
    with pytest.raises(ValueError):
        Customer("")

def test_customer_invalid_name_length_2():
    with pytest.raises(ValueError):
        Customer("This name is too long to be valid")

def test_customer_orders():
    customer = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    order1 = customer.create_order(coffee1, 5.0)
    order2 = customer.create_order(coffee2, 4.0)
    assert order1 in customer.orders()
    assert order2 in customer.orders()

def test_customer_coffees():
    customer = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 4.0)
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_customer_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
