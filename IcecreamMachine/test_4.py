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
    machine.handle_flavor("vanilla")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    assert machine.remaining_scoops==0

@pytest.fixture
def second_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    machine.handle_pay(5.25,"5.25")
    return machine

def test_max_scoops_order(second_order):
    assert second_order is not None

#Test 4