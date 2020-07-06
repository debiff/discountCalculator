import unittest
import json
from discount_calculator import compute_discount


class TestDiscountMethod(unittest.TestCase):
    def setUp(self):
        with open("./samples/bundles.json") as f:
            self.discount_bundles = list(json.load(f))

        with open("./samples/products.json") as f:
            self.products_list = list(json.load(f))

    def test_void_bundle(self):
        cart = "ABC"
        total_discount = compute_discount([], self.products_list, cart)
        self.assertEqual(total_discount, 0)

    def test_void_product_list(self):
        cart = "ABC"
        total_discount = compute_discount(self.discount_bundles, [], cart)
        self.assertEqual(total_discount, 0)

    def test_void_cart(self):
        cart = ""
        total_discount = compute_discount(
            self.discount_bundles, self.products_list, cart
        )
        self.assertEqual(total_discount, 0)


if __name__ == "__main__":
    unittest.main()
