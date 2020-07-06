# Created by Simone Biffi at 7/6/20


def compute_discount(bundles: list, products: list, cart: str) -> float:
    """
    Calculate the total applicable discount to a set of product
    :param bundles: list
    :param products: list
    :param cart_items: str
    :return: float -> the total discount in euro
    """

    if type(bundles) is not list or type(products) is not list or type(cart) is not str:
        raise TypeError

    total_discount: float = 0

    # Get list of cart item from the input string of ids
    cart_items: list = cart.replace(" ", "").split(",")

    # Convert the list of products in a dict of product.
    products_prices: dict = {product["sku"]: product["price"] for product in products}

    # Get the applicable bundles
    applicable_bundles: list = []

    if len(applicable_bundles) > 0:
        pass
    elif len(cart_items) > 5:
        # If there isn't a bundle and in the cart there are more than 5 elements, apply 6% discount
        # to all products in the cart
        applicable_discount = 0.06
        total_discount = sum(
            [products_prices[item] * applicable_discount for item in cart_items]
        )

    return round(total_discount, 2)
