from models import Customer, Menu, MenuItem, Order


def test_order_total():
    order = Order()

    burger = MenuItem("Burger", 8.99, "Food", 4.5)
    soda = MenuItem("Soda", 2.50, "Drinks", 4.0)

    order.add_item(burger)
    order.add_item(soda)

    assert order.compute_total() == 11.49

def test_empty_order_total():
    order = Order()

    assert order.compute_total() == 0

def test_filter_by_category():
    menu = Menu()

    burger = MenuItem("Burger", 8.99, "Food", 4.5)
    soda = MenuItem("Soda", 2.50, "Drinks", 4.0)
    coffee = MenuItem("Coffee", 3.50, "Drinks", 4.8)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(coffee)

    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 2
    assert [item.name for item in drinks] == ["Soda", "Coffee"]

def test_sort_by_popularity():
    menu = Menu()

    burger = MenuItem("Burger", 8.99, "Food", 4.5)
    soda = MenuItem("Soda", 2.50, "Drinks", 4.0)
    coffee = MenuItem("Coffee", 3.50, "Drinks", 4.8)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(coffee)

    popular_items = menu.sort_by_popularity()

    assert [item.name for item in popular_items] == [
        "Coffee", "Burger", "Soda"
    ]
def test_customer_purchase_history():
    customer = Customer("Alex")

    assert customer.has_purchase_history() == False

    order = Order()
    customer.add_order(order)

    assert customer.has_purchase_history() == True
    assert len(customer._purchase_history) == 1