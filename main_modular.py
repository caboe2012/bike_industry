from bike_classes import *
import random


def create_bikes():
    ''' Instantiate 8 different Bicycle classes '''
    road = Bicycle("road", 5, 200)
    dirt = Bicycle("dirt", 8,100)
    race = Bicycle("race",3, 500)
    grinder = Bicycle("grinder", 10, 300)
    hybrid = Bicycle("hybrid", 6, 150)
    bmx = Bicycle("bmx",4, 400)
    tandem = Bicycle("tandem", 20, 600)
    mtn = Bicycle("mountain", 10, 475)
    models = [road, dirt, race, grinder, hybrid, bmx, tandem, mtn]
    return models

def create_bikeshop(bikes, name, qty, marg=.2, prof=0, budg=10000):
    ''' Instantiate first Bike Shop class '''
    all_bikes = {}
    for bike in bikes:
        all_bikes[bike] = qty
    shop = Bike_Shop(name, inventory = all_bikes, margin = marg, profit = prof, budget = budg)
    return shop

def create_customers():
    ''' Create 3 instances of the Customer class '''
    Chad = Customers("Chad", 300)
    Rachel = Customers("Rachel", 600)
    Drew = Customers("Drew", 1000)
    clients = [Chad, Rachel, Drew]
    print "In this basic version of the Bicycle Industry there are the following {} customers.".format(len(clients))
    print "{} and {}.".format(", ".join(person.name for person in clients[:-1]), clients[-1].name)
    print
    return clients

def affordable_bike_options(customers, shop):
    ''' Print the name of each customer and a list of the bikes 
    that they can afford at the bike shop '''
    affordable_bikes = {}
    for person in customers:
        temp = []
        for bike in shop.inventory:
            sale_price = bike.cost + bike.cost*shop.margin
            if sale_price <= person.fund:
                temp.append(bike)
        print "{} can afford the following {} bikes at {}:".format(person.name, len(temp), shop.name)
        for bike in temp:
            print "- {}".format(bike.model)
        affordable_bikes[person] = temp
        print
    return affordable_bikes

def print_shop_inventory(shop):
    ''' Print out current invetory of bikes at Bike Class instance '''
    shop.stock()
    print 

def buy_a_bike(bike_options, shop):    
    ''' Each customer purchases 1 bike, print out the model how much it cost and how
    much money is left each customers fund.'''
    for person, bikes in bike_options.items():
        choice = random.choice(bikes)
        sale_price = choice.cost + choice.cost*shop.margin
        person.fund -= sale_price
        person.rides.append(choice)
        shop.inventory[choice] -= 1
        shop.profit += choice.cost*shop.margin
        print "{} bought a {} bike for ${} and now has ${} remaining.".format(person.name, choice.model, str(sale_price), str(person.fund))
        print    
    #return shop

def shop_profits(shop):
    ''' After selling all three bikes, print out the new inventory at the bike shop and 
    how much profit was made on the sale of all three'''
    print "After selling all three bikes, {} made ${} in total profit.".format(shop.name, str(shop.profit))
    print
    shop.stock()

if __name__ == "__main__":
    bike_types = create_bikes()
    bike_store = create_bikeshop(bike_types, "Sternlandia", 3, marg=.2, prof=0, budg=10000)
    people = create_customers()
    affordable_choices = affordable_bike_options(people, bike_store)
    print_shop_inventory(bike_store)
    buy_a_bike(affordable_choices, bike_store)
    shop_profits(bike_store)
    