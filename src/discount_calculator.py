# Created by Simone Biffi at 7/6/20
from collections import Counter


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
    applicable_bundles: list = list(
        filter(
            lambda bundle: len(
                list((Counter(bundle["products"]) - Counter(cart_items)).elements())
            )
            == 0,
            bundles,
        )
    )

    if len(applicable_bundles) > 0:
        # Calculate total discount for each applicable bundle
        for current_bundle in applicable_bundles:
            products_total_price: float = sum(
                [products_prices[item_id] for item_id in current_bundle["products"]]
            )
            current_bundle["total_discount"] = (
                products_total_price * current_bundle["discount"]
            )

        # Order applicable bundle by total discount and take the max
        applicable_bundles = sorted(
            applicable_bundles,
            key=lambda bundle: bundle["total_discount"],
            reverse=True,
        )
        total_discount = applicable_bundles[0]["total_discount"]

    elif len(cart_items) > 5:
        # If there isn't a bundle and in the cart there are more than 5 elements, apply 6% discount
        # to all products in the cart
        applicable_discount = 0.06
        total_discount = sum(
            [products_prices[item] * applicable_discount for item in cart_items]
        )

    return round(total_discount, 2)
