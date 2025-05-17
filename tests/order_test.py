import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_order_attributes(self):
        customer = Customer("Charity")
        coffee = Coffee("Black Coffee")
        order = Order(customer, coffee, 5.0)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
        
        with pytest.raises(AttributeError):
            order.price = 6.0
            
        with pytest.raises(TypeError):
            Order("not customer", coffee, 5.0)