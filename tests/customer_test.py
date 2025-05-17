import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_name(self):
        customer = Customer("Charity")
        assert customer.name == "Charity"
        
        with pytest.raises(TypeError):
            Customer(123)
            
        with pytest.raises(ValueError):
            Customer("")
            
    def test_create_order(self):
        customer = Customer("Charity")
        coffee = Coffee("Black Coffee")
        order = customer.create_order(coffee, 5.0)
        
        assert order in Order.all
        assert order.customer == customer
        assert order.coffee == coffee