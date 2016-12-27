from bicycle_classes import *
import random



''' Instantiate 8 different Bicycle classes '''
road = Bicycle("road", 5, 200)
dirt = Bicycle("dirt", 8,100)
race = Bicycle("race",3, 500)
grinder = Bicycle("grinder", 10, 300)
hybrid = Bicycle("hybrid", 6, 150)
bmx = Bicycle("bmx",4, 400)
tandem = Bicycle("tandem", 20, 600)
mtn = Bicycle("mountain", 10, 475)

''' Instantiate first Bike Shop class '''
all_bikes = {road:3, dirt:3, race:3, grinder:3, hybrid:3, bmx:3, tandem:3, mtn:3}
papillon = Bike_Shop("Papillon", inventory = all_bikes, margin = .2,profit = 0, budget = 10000)

''' Create 3 instances of the Customer class '''
Chad = Customers("Chad", 300)
Rachel = Customers("Rachel", 600)
Drew = Customers("Drew", 1000)
CLIENTS = [Chad, Rachel, Drew]
print "In this basic version of the Bicycle Industry there are the following {} customers.".format(len(CLIENTS))
print "{} and {}.".format(", ".join(person.name for person in CLIENTS[:-1]), CLIENTS[-1].name)
print

''' Print the name of each customer and a list of the bikes 
that they can afford at the bike shop '''
for person in CLIENTS:
    affordable_bikes = []
    for bike in papillon.inventory:
        sale_price = bike.cost + bike.cost*papillon.margin
        if sale_price <= person.fund:
            affordable_bikes.append(bike)
    print "{} can afford the following {} bikes at {}:".format(person.name, len(affordable_bikes), papillon.name)
    for bike in affordable_bikes:
        print "- {}".format(bike.model)
    print


''' Print out current invetory of bikes at Bike Class instance '''
papillon = Bike_Shop("Papillon", inventory = all_bikes, margin = .2,profit = 0, budget = 10000)
papillon.stock()
print

''' Each customer purchases 1 bike, print out the model how much it cost and how
much money is left each customers fund.'''
for person in CLIENTS:
    affordable_bikes = []
    for bike in papillon.inventory:
        sale_price = bike.cost + bike.cost*papillon.margin
        #print "{} has a cost of {} and sells for {}".format(bike.name, bike.cost, sale_price)
        if sale_price <= person.fund:
            affordable_bikes.append(bike)
#            print "The {} cost of {} with a {} margin = {}" .format(bike.name,bike.cost, papillon.margin, str(sale_price)) 
    choice = random.choice(affordable_bikes)
    sale_price = choice.cost + choice.cost*papillon.margin
    person.fund -= sale_price
    person.rides.append(choice)
    papillon.inventory[choice] -= 1
    papillon.profit += choice.cost*papillon.margin
    print "{} bought a {} bike for ${} and now has ${} remaining.".format(person.name, choice.model, str(sale_price), str(person.fund))
print    


''' After selling all three bikes, print out the new inventory at the bike shop and 
how much profit was made on the sale of all three'''
print "After selling all three bikes, {} made ${} in total profit.".format(papillon.name, str(papillon.profit))

papillon.stock()

