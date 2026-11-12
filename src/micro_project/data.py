# Simulated database of menu items
from micro_project.schema import MenuItem


menu_items = [
    MenuItem(id=1, name='Margherita Pizza', category='pizza', price=8.99, available=True),
    MenuItem(id=2, name='Caesar Salad', category='salad', price=5.99, available=True),
    MenuItem(id=3, name='Spaghetti Bolognese', category='pasta', price=10.99, available=True),
    MenuItem(id=4, name='Grilled Chicken Sandwich', category='sandwich', price=7.99, available=False),
    MenuItem(id=5, name='Chocolate Brownie', category='dessert', price=3.99, available=True),
    MenuItem(id=6, name='Margarita', category='drink', price=4.99, available=True),
    MenuItem(id=7, name='Pepperoni Pizza', category='pizza', price=9.99, available=True),
]
