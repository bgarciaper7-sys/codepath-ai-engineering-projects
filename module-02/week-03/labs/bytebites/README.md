# ByteBites: Campus Food Ordering System

## Project Overview

ByteBites is a Python-based campus food ordering system developed as part of a CodePath AI Engineering 101 Tinker activity.

The project focuses on object-oriented programming (OOP), algorithm implementation, UML design, debugging, and automated testing.

I designed and implemented Python classes to represent customers, menu items, menus, and orders. I also developed algorithms for calculating order totals, filtering menu items by category, sorting items by popularity, and tracking customer purchase history.

## Technologies & Tools

- Python
- pytest
- Mermaid UML
- Visual Studio Code
- Git
- GitHub Copilot for initial design exploration

## Key Features

**Order Management**
- Add menu items to an order.
- Calculate the total price of an order.
- Handle empty orders.

**Menu Management**
- Add menu items with names, prices, categories, and popularity ratings.
- Filter menu items by category.
- Sort menu items by popularity rating.

**Customer Management**
- Create customer objects.
- Record orders in customer purchase history.
- Check whether a customer has previous orders.

## Object-Oriented Design

The system contains four main classes:

| Class | Responsibility |
|---|---|
| Customer | Stores customer information and purchase history |
| MenuItem | Represents an individual food or drink |
| Menu | Manages and organizes available menu items |
| Order | Stores ordered items and calculates totals |

The project includes an initial UML draft and a refined Mermaid UML diagram.

## Automated Testing

I implemented five automated tests using pytest:

1. Order total calculation
2. Empty order total
3. Menu category filtering
4. Menu sorting by popularity
5. Customer purchase history

**Latest verified result: 5 tests passed.**

To run the tests:

```bash
python -m pytest test_bytebites.py -v
```

## Challenges & Debugging

One issue I encountered was in the `filter_by_category()` method. The `return` statement was incorrectly indented inside the loop, causing the function to stop after finding the first matching item.

I corrected the indentation and verified that the function returned all matching menu items.

I also debugged an indentation error in my pytest file and reran the tests successfully.

## What I Learned

Through this project, I practiced:

- Designing classes and objects
- Using constructors and instance attributes
- Working with lists and loops
- Writing methods with return values
- Using sorting algorithms and lambda functions
- Debugging Python
