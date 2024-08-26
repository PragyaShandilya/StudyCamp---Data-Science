class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self, order_id, customer, list_of_items):
        self.order_id = order_id
        self.customer = customer
        self.list_of_items = list_of_items
        self.total_price = sum(item.price for item in list_of_items)

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.order_list = []

    def add_order(self, order):
        self.order_list.append(order)

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        order.customer.add_order(order)
        print(f"Order {order.order_id} added for customer {order.customer.name}.")

    def calc_tot_sales(self):
        total_sales = sum(order.total_price for order in self.orders)
        print(f"Total Sales = {total_sales}")

#---------------------------------------------------------------------------------------------------------------
# Creating menu items
item1 = MenuItem('Pancake', 100, 'Breakfast')
item2 = MenuItem('Rice and Manchurian', 200, 'Lunch')
item3 = MenuItem('Pao Bhaji', 300, 'Dinner')
item4 = MenuItem('Ice Cream', 50, 'Dessert')

# Creating a customer
cust1 = Customer('ABC', 852799)

# Creating orders
order1 = Order(1, cust1, [item1, item2])
order2 = Order(2, cust1, [item3])

# Creating the restaurant and adding orders
restaurant = Restaurant([item1, item2, item3, item4])
restaurant.add_order(order1)
restaurant.add_order(order2)

# Calculating total sales
restaurant.calc_tot_sales()
