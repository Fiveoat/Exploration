from order import Order

class Customer():
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        count = 0
        for order in self.orders:
            count += 1
        return count

    def get_total(self):
        total = 0
        for order in self.orders:
            totals = order.get_total()
            total += totals
        return total

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print(f"Summary for customer '{self.id}':")
        print(f"Name: {self.name}")
        print(f"Orders: {self.get_order_count()}")
        print(f"Total: {format(self.get_total(),'.2f')}")

    def display_receipts(self):
        print(f"Detailed receipts for customer '{self.id}':")
        print(f"Name: {self.name}")
        print("")
        for order in self.orders:
            order.display_receipt()
            print("")