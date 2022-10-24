from importlib import machinery
import pytest
from IcecreamMachine import STAGE, Flavor, IceCreamMachine, Toppings

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

def test_first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == 2.25

def test_second_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == 3.25

def test_third_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("sprinkles")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == 2.5