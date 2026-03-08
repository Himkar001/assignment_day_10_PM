"""
Bug Fix Example
Original issues:
1. Mutable default argument
2. Scope issue with global variable
"""

total = 0


def add_to_cart(item, cart=None):

    global total

    if cart is None:
        cart = []

    cart.append(item)

    total = total + len(cart)

    return cart


print(add_to_cart("apple"))
print(add_to_cart("banana"))