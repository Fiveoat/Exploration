from product import Product

class Order():
    def __init__(self):
        self.id = ""
        self.products = []

    def get_subtotal(self):
        subtotal = 0
        for item in self.products:
            price = item.get_total_price()
            subtotal += price
        return subtotal


    def get_tax(self):
        subtotal = self.get_subtotal()
        tax = subtotal * .065
        return tax

    def get_total(self):
        subtotal = self.get_subtotal()
        tax = self.get_tax()
        total = tax + subtotal
        return total

    def add_product(self, Product):
        self.products.append(Product)

    def display_receipt(self):
        # items = Product()
        print(f"Order: {self.id}")
        for item in self.products:
            item.display()
        print(f"Subtotal: ${format(self.get_subtotal(),'.2f')}")
        print(f"Tax: ${format(self.get_tax(),'.2f')}")
        print(f"Total: ${format(self.get_total(),'.2f')}")

