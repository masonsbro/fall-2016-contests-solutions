from collections import defaultdict, namedtuple

Pin = namedtuple('Pin', ['cost', 'needed_supplies'])
Supply = namedtuple('Supply', ['quantity', 'price'])

def main():
    cases = int(input())

    for _ in range(cases):
        num_pins, num_supplies, num_orders = map(int, input().split())
        pins = {}
        supplies = {}
        owned = defaultdict(int)

        for _ in range(num_pins):
            name, cost = input().split()
            cost = int(cost)

            needed_supplies = set(input().split())
            pins[name] = Pin(cost, needed_supplies)

        for _ in range(num_supplies):
            name, quantity, price = input().split()
            quantity, price = int(quantity), int(price)
            supplies[name] = Supply(quantity, price)

        total_costs = 0
        revenue = 0

        for _ in range(num_orders):
            name, quantity = input().split()
            quantity = int(quantity)

            pin = pins[name]
            revenue += quantity * pin.cost

            for supply_name in pin.needed_supplies:
                supply = supplies[supply_name]
                if owned[supply_name] < quantity:
                    needed = quantity - owned[supply_name]
                    units_to_buy = needed // supply.quantity
                    if needed % supply.quantity != 0:
                        units_to_buy += 1

                    total_costs += units_to_buy * supply.price
                    owned[supply_name] += units_to_buy * supply.quantity

                owned[supply_name] -= quantity

        print(revenue - total_costs)

main()
