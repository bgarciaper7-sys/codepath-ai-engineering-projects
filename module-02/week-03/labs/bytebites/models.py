# ByteBites - Campus Food Ordering Application
#
# Classes to implement:
# 1. Customer
# 2. MenuItem
# 3. Menu
# 4. Order


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Order:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def compute_total(self):
        return sum(item.price for item in self._items) 


class Menu:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def filter_by_category(self, category):
        matching_items = []
        for item in self._items:
            if item.category == category:
                matching_items.append(item)
                
        return matching_items

    def sort_by_popularity(self):
        return sorted(
            self._items,
            key=lambda item: item.popularity_rating,
            reverse=True
        )
        


class Customer:
    def __init__(self, name):
        self._name = name
        self._purchase_history = []

    def add_order(self, order):
        self._purchase_history.append(order)

    def has_purchase_history(self):
        return len(self._purchase_history) > 0
