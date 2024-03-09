"""Functions to manage a users shopping cart items."""


def add_items(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    new_dict = {item: items_to_add.count(item) for item in items_to_add}
    keys = {**current_cart, **new_dict}.keys()
    return {key: current_cart.get(key, 0) + new_dict.get(key, 0) for key in keys}


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    update_ideas_with = dict(recipe_updates)
    new_ideas = ideas | update_ideas_with
    return new_ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    pass


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    pass


### PRUEBAS
# print(add_items({'Banana': 3, 'Apple': 2, 'Orange': 1},('Apple', 'Apple', 'Orange', 'Apple', 'Banana')))
# print(add_items({'Banana': 3, 'Apple': 2, 'Orange': 1},['Banana', 'Orange', 'Blueberries', 'Banana']))
# print(read_notes(('Banana','Apple', 'Orange')))
# print(read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple']))

# test_1 = update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
# (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
# result_1 = {'Banana Bread' : {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3},
#  'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}
# print(test_1)
# print(test_1 == result_1)   

print(sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1}))