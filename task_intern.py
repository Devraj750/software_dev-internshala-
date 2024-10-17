# SYSTEM DESIGN 


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)

    def view_orders(self):
        for order in self.orders:
            print(order)


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = []
        self.status = 'Pending'
        self.payment = None

    def add_product(self, product):
        self.products.append(product)

    def make_payment(self, payment):
        self.payment = payment
        self.status = 'Completed'


class Payment:
    def __init__(self, payment_id, amount):
        self.payment_id = payment_id
        self.amount = amount
        self.status = 'Pending'

    def complete_payment(self):
        self.status = 'Completed'


if __name__ == "__main__":
    
    user = User(1, "John Doe", "john@example.com")
    
    
    product1 = Product(101, "Laptop", 1500)
    product2 = Product(102, "Smartphone", 800)
    
 
    order = Order(1001)
    order.add_product(product1)
    order.add_product(product2)
    

    user.create_order(order)
   
    payment = Payment(201, 2300)  
    order.make_payment(payment)
    
    
    payment.complete_payment()

    
    user.view_orders()



# Business Logic for Inventory Management System


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError(f"Not enough stock for {self.name}. Current stock: {self.stock}")

    def restock(self, quantity):
        self.stock += quantity
def process_orders(products, orders, threshold=10):
    """
    Reduces stock levels based on incoming orders.
    Args:
    - products: List of Product objects.
    - orders: Dictionary where key is product_id and value is the quantity ordered.
    - threshold: Stock level threshold to trigger a restock alert.
    
    Raises:
    - ValueError: If an order quantity exceeds available stock.
    """
    alerts = []
    
    for product_id, quantity in orders.items():
        product = next((p for p in products if p.product_id == product_id), None)
        
        if product:
            try:
                product.reduce_stock(quantity)
                print(f"Order processed for {product.name}, {quantity} units.")
                
                
                if product.stock < threshold:
                    alerts.append(f"Alert: {product.name} stock below {threshold} units (Current stock: {product.stock})")
            
            except ValueError as e:
                print(e)
        else:
            print(f"Product ID {product_id} not found in inventory.")
    
     
    for alert in alerts:
        print(alert)
def restock_items(products, restock_list):
    """
    Restocks items in the inventory.
    Args:
    - products: List of Product objects.
    - restock_list: Dictionary where key is product_id and value is the quantity to restock.
    """
    for product_id, quantity in restock_list.items():
        product = next((p for p in products if p.product_id == product_id), None)
        
        if product:
            product.restock(quantity)
            print(f"{product.name} restocked by {quantity} units. Current stock: {product.stock}")
        else:
            print(f"Product ID {product_id} not found in inventory.")

if __name__ == "__main__":

    products = [
        Product(101, "Laptop", 1500, 20),
        Product(102, "Smartphone", 800, 5),
        Product(103, "Tablet", 600, 12)
    ]
    
     
    orders = {
        101: 5,  # Order 5 Laptops
        102: 2,  # Order 2 Smartphones
        103: 15  # Order 15 Tablets (this will exceed stock)
    }
    
    
    process_orders(products, orders)
    
    
    restock_list = {
        102: 10,
        103: 20   
    }
    
    restock_items(products, restock_list)
