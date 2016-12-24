import random

class Bicycle(object):
    def __init__(self,model,weight,cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
class Bike_Shop(object):
    def __init__(self, name, inventory = [], margin = .2, profit = 0, budget = 10000):
        self.name = name
        self.inventory = inventory
        self.margin = margin
        self.profit = profit
        self.budget = budget
        self.spend = 0
    
    def buy(self, bike):
        self.inventory.append(bike)
        self.budget -= bike.cost
        self.spend += bike.cost
    
    def sell(self,bike):
        self.inventory.remove(bike)
        self.profit += bike.cost +  bike.cost*margin
    
    def stock(self):
        if len(self.inventory) == 0:
            print "Sorry. All of our bikes are on back-order."
            print "The next shipment should arrive next Wednesday."
        else:
            print "The folowing {} bikes are currently in stock at {}:".format(len(self.inventory),self.name)
            print ", ".join([each.name for each in self.inventory])
    def profit(self):
        print "Annual profit for the year-to-date is ${} USD.".format(self.profit)
    
    def spend(self):
        print "Annual spend for the year-to-date is ${} USD.".format(self.spend)

        
class Customers(object):
    def __init__(self,name,fund = 200,rides = []):
        self.name = name
        self.fund = fund
        self.rides = rides

