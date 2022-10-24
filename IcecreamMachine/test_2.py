from importlib import machinery
import pytest
from IcecreamMachine import STAGE, Flavor, IceCreamMachine, Toppings


@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

@pytest.fixture
def first_order(machine):
    machine.flavors[0].quantity=2
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    #machine.handle_flavor("vanilla")
    #machine.handle_flavor("vanilla")
    #machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    return machine

def test_maximum_flavors(first_order):
    return first_order is not None

#Test 2