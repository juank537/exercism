"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for i in items:
        inventory[i] = items.count(i)
    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    items_to_add = create_inventory(items)
    keys = inventory.keys()
    for key, value in items_to_add.items():
        if key in keys:
            inventory[key] += value
        else:
            inventory[key] = value
    return inventory   



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    items_to_rest = create_inventory(items)
    keys = inventory.keys()
    for key, value in items_to_rest.items():
        if key in keys:
            inventory[key] -= value
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    return inventory.pop(item)


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return list(inventory.items())



# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))
# print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
# print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))

print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))