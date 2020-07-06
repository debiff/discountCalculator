# Created by Simone Biffi at 7/6/20
import click
import json
from src.discount_calculator import compute_discount


@click.command()
@click.option(
    "--bundles",
    type=click.Path(exists=True, readable=True),
    default="./samples/bundles.json",
    help="Location of JSON file containing the bundles",
)
@click.option(
    "--products",
    type=click.Path(exists=True, readable=True),
    default="./samples/products.json",
    help="Location of JSON file containing the products",
)
@click.option(
    "--cart", default="", help="The products in the cart. Should be comma separated."
)
def main(bundles, products, cart):
    """Calculates the applicable discount given a list of discount bundle,
    a list of product and the products in the cart
    """
    with open(bundles) as f:
        discount_bundles = list(json.load(f))

    with open(products) as f:
        products_list = list(json.load(f))

    click.echo(
        "The total discount is: "
        + str(compute_discount(discount_bundles, products_list, cart))
        + "€"
    )
