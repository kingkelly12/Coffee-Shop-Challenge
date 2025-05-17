import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_coffee_name(self):
        coffee = Coffee("Black Coffee")
        assert coffee.name == "Black Coffee"
        with pytest.raises(TypeError):
            Coffee(123)
            
        with pytest.raises(ValueError):
            Coffee("A")
            
        with pytest.raises(AttributeError):
            coffee.name = "New Name"
            
    def test_num_orders(self):
        coffee = Coffee("Black Coffee")
        assert coffee.num_orders() == 0
        
        customer = Customer("Charity")
        Order(customer, coffee, 5.0)
        assert coffee.num_orders() == 1