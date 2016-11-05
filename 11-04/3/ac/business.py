class Business():
    def __init__(self):
        self.pin_to_price = {}
        self.pin_to_supplies = {}
        self.supply_to_price = {}
        self.supply_to_bulk = {}
        self.supply_inventory = {}
        self.revenue = 0
        self.costs = 0

    def add_pin(self, pin, price):
        self.pin_to_price[pin] = price

    def add_supplies(self, pin, supplies):
        self.pin_to_supplies[pin] = supplies

    def add_supply(self, supply, bulk_amount, price):
        self.supply_to_price[supply] = price
        self.supply_to_bulk[supply] = bulk_amount
        self.supply_inventory[supply] = 0

    def order(self, pin, amount):
        for supply in self.pin_to_supplies[pin]:
            while self.supply_inventory[supply] < amount:
                self.supply_inventory[supply] += self.supply_to_bulk[supply]
                self.costs += self.supply_to_price[supply]
            self.supply_inventory[supply] -= amount
        self.revenue += self.pin_to_price[pin] * amount

    def profit(self):
        return self.revenue - self.costs

def main():
    t = int(input())
    for i in range(t):
        b = Business()
        n, m, o = map(int, input().split())
        for j in range(n):
            pin, price = map(int, input().split())
            b.add_pin(pin, price)
            supplies = list(map(int, input().split()))
            b.add_supplies(pin, supplies)
        for j in range(m):
            supply, bulk, price = map(int, input().split())
            b.add_supply(supply, bulk, price)
        for j in range(o):
            pin, amount = map(int, input().split())
            b.order(pin, amount)
        print(b.profit())

main()
