from enum import Enum
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException("Sorry for the inconvinience caused, we are out of stock for now")
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0

class Container(Usable):
    pass

class Flavor(Usable):
    pass

class Toppings(Usable):
    pass

class STAGE(Enum):
    Container = 1
    Flavor = 2
    Toppings = 3
    Pay = 4

class IceCreamMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 100
    MAX_SCOOPS = 3
    MAX_TOPPINGS = 3


    containers = [Container(name="Waffle Cone", cost=1.5), Container(name="Sugar Cone", cost=1), Container("Cup", cost=1)]
    flavors = [Flavor(name="Vanilla", quantity=100, cost=1), Flavor(name="Chocolate", quantity=100, cost=1), Flavor(name="Strawberry", quantity=100, cost=1)]
    toppings = [Toppings(name="Sprinkles", quantity=200, cost=.25), Toppings(name="Chocolate Chips", quantity=200, cost=.25), Toppings(name="M&Ms", quantity=200, cost=.25), \
    Toppings(name="Gummy Bears", quantity=200, cost=.25), Toppings(name="Peanuts", quantity=200, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_scoops = MAX_SCOOPS
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_icecreams = 0

    inprogress_icecream = []
    currently_selecting = STAGE.Container

    # rules
    # 1 - container must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - scoops can't exceed max
    # 4 - toppings can't exceed max
    # 5 - a container and at least 1 scoop or toppings must be selected
    # 6 - proper cost must be calculated and shown to the user
    # 7 - cleaning must be done after certain number of uses before any more icecreams can be made
    # 8 - total sales should calculate properly based on cost calculation
    # 9 - total_icecreams should increment properly after a payment
    

    def pick_container(self, choice):
        for c in self.containers:
            if c.name.lower() == choice:
                try:
                    c.use()
                    self.inprogress_icecream.append(c)
                    return
                except:
                    raise OutOfStockException("Sorry but the item which you are chosing is not available, please pick other options")
        raise InvalidChoiceException("Please enter a valid container choice from the provided options")

    def pick_flavor(self, choice):
        try:
            if self.remaining_uses <= 1:
                clean_input=input("System needs to be clean before processing the order, please enter 'yes' to clean ").strip().lower()
                if clean_input=="yes":
                    raise NeedsCleaningException("Thank you, cleaning is now completed")
                else:
                    while clean_input!="yes":
                        clean_input=input("System needs to be clean before processing the order, please enter 'yes' to clean ").strip().lower()
                    raise NeedsCleaningException("Thank you, cleaning is now completed")
        except NeedsCleaningException as e:
            print(e)
            self.clean_machine()
        
        try:
            if self.remaining_scoops <= 1:
                raise ExceededRemainingChoicesException("You have reached the maximum flavor choices, please select toppings now")
        except ExceededRemainingChoicesException as e:
            print(e)
            self.currently_selecting = STAGE.Toppings

        for f in self.flavors:
            if f.name.lower() == choice:
                try:
                    f.use()
                    self.inprogress_icecream.append(f)
                    self.remaining_scoops -= 1
                    self.remaining_uses -= 1
                    return
                except:
                    raise OutOfStockException("Sorry but the flavor which you are chosing is not available, please pick other flavor options")            
        raise InvalidChoiceException("Please enter a valid flavor choice from the provided options")

    def pick_toppings(self, choice):
        try:
            if self.remaining_toppings <= 1:
                raise ExceededRemainingChoicesException("You have reached the maximum topping choices, please pay now")
        except ExceededRemainingChoicesException as e:
            print(e)
            self.currently_selecting = STAGE.Pay

        for t in self.toppings:
            if t.name.lower() == choice:
                try:
                    t.use()
                    self.inprogress_icecream.append(t)
                    self.remaining_toppings -= 1
                    return
                except:
                    raise OutOfStockException("Sorry but the topping which you are chosing is not available, please pick other toppings options")
        raise InvalidChoiceException("Please enter a valid toppings choice from the provided option")

    def reset(self):
        self.remaining_scoops = self.MAX_SCOOPS
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_icecream = []
        self.currently_selecting = STAGE.Container

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_container(self, container):
        try:
            self.pick_container(container)
            self.currently_selecting = STAGE.Flavor
        except (InvalidChoiceException, OutOfStockException) as e:
            print(e)
            self.currently_selecting = STAGE.Container

    def handle_flavor(self, flavor):
        try:
            if flavor == "next":
                self.currently_selecting = STAGE.Toppings
            else:
                self.pick_flavor(flavor)
        except (InvalidChoiceException, OutOfStockException) as e:
            print(e)
            self.currently_selecting = STAGE.Flavor

    def handle_toppings(self, toppings):
        try:
            if toppings == "done":
                self.currently_selecting = STAGE.Pay
            else:
                self.pick_toppings(toppings)
        except (InvalidChoiceException, OutOfStockException) as e:
            print(e)
            self.currently_selecting = STAGE.Toppings

    def handle_pay(self, expected, total):
        if total == str(expected):
            print("Thank you! Enjoy your icecream!")
            self.total_icecreams += 1
            self.total_sales += expected # only if successful
            self.reset()
            return
        raise InvalidPaymentException("Please enter the exact payment value")
            
    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_icecream
        # sp2943  October 23, 2022
        
        if self.inprogress_icecream[0].name == 'Waffle Cone':
            price_of_cone = 1.5
        else:
            price_of_cone = 1.0
            
        price_of_flavor = self.flavors[0].cost
        price_of_toppings = self.toppings[0].cost
        
        scoops_consumed = self.MAX_SCOOPS - self.remaining_scoops
        toppings_used = self.MAX_TOPPINGS - self.remaining_toppings
        
        total_cost = price_of_cone + (scoops_consumed)*(price_of_flavor) + (toppings_used)*(price_of_toppings)
        
        return total_cost

    def run(self):
        if self.currently_selecting == STAGE.Container:
            container = input(f"Would you like a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
            self.handle_container(container)
        elif self.currently_selecting == STAGE.Flavor:
            flavor = input(f"Would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
            self.handle_flavor(flavor)
        elif self.currently_selecting == STAGE.Toppings:
            toppings = input(f"Would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
            self.handle_toppings(toppings)
            if self.remaining_scoops==3 and self.remaining_toppings==3:
                print ("Sorry, but you will have to select at least one flavor or toppings, container can't be empty")
                self.currently_selecting=STAGE.Flavor
                self.run()
        elif self.currently_selecting == STAGE.Pay:
            expected = self.calculate_cost() 
            total = input(f"Your total is ${expected}, please enter the exact value.\n")

            try:
                self.handle_pay(expected, total)
            except InvalidPaymentException as e:
                print(e)
                self.run()
            choice = input("What would you like to do? (icecream or quit)\n")
            if choice == "quit":
                exit()
        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    icm = IceCreamMachine()
    icm.start()