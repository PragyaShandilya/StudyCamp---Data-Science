#Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price

class Shopping_Cart:
    def __init__(self, items):
        self.items = items
        self.price = 0
        for item in items:
            self.price += items[item]
        print("Total current price:", self.price)


    def remove(self):
        item = input("Enter item to remove: ")
        if item in self.items:
            print("Removing", item)
            self.price -= self.items[item]
            self.items.pop(item)
            print("Items after removal:", self.items)
        else:
            print("Item not found in the cart.")

    def add(self,item):
        item = input("Enter item to add: ")
        Price = int(input("Price of item is "))
        self.items[item] = Price
        self.price = self.price = Price
        print(self.items)

current = {'Cake':100, 'Butter':200, 'Apple':400, 'Onions':500}
obj1 = Shopping_Cart(current)