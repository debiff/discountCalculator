# Created by Simone Biffi at 7/6/20


def compute_discount(bundles: list, products: list, cart_items: str) -> float:
    """
    Calculate the total applicable discount to a set of product
    :param bundles: list
    :param products: list
    :param cart_items: str
    :return: float -> the total discount in euro
    """

    if (
        type(bundles) is not list
        or type(products) is not list
        or type(cart_items) is not str
    ):
        raise TypeError

    total_discount: float = 0

    # Get list of cart item from the input string of ids
    cart_item_list: list = cart_items.replace(" ", "").split(",")

    print(cart_item_list)
    return total_discount
