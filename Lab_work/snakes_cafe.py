print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

***********************************
**  Type 'quit' to exit the app. **
***********************************
""")

order = input("> ")

menu = {
    "wings": 0, "cookies": 0, "spring Rolls": 0,
    "salmon": 0, "steak": 0, "meat tornado": 0,
    "A literal garden": 0, "ice cream": 0, "cake": 0,
    "pie": 0, "coffee": 0, "tea": 0, "unicorn tears": 0,
}

final_order = {}

while order:
    if order == "quit":
        break

    elif order in menu:
        menu[order] += 1
        final_order[order] = menu[order]
        order = input(f"""
********************************************
You ordered {menu[order]} {order}, anything else?
********************************************

> """)
    elif order not in menu:
        order = input(f"""
********************************************
That is not on the menu, please try again...
********************************************

> """)

print(f"""
********************************************
            Your final order is
""")

for key, value in final_order.items():
    print(value, key)

print(f"""
            Thanks for coming!
********************************************
""")
