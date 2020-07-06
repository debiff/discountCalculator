import unittest
import json
from discount_calculator import compute_discount


class TestDiscountMethod(unittest.TestCase):
    def setUp(self):
        with open("../samples/bundles.json") as f:
            self.discount_bundles = list(json.load(f))

        with open("../samples/products.json") as f:
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

    def test_incorrect_parameter_type(self):
        with self.assertRaises(TypeError):
            compute_discount(
                self.discount_bundles, self.products_list, ["LNIAL-8393,JSVVX-8355"]
            )

    def test_single_bundle_match(self):
        cart = "HWKAM-9680,UGSXO-1999"
        total_discount = compute_discount(
            self.discount_bundles, self.products_list, cart
        )
        self.assertEqual(total_discount, 46.77)

    def test_different_order_single_bundle_match(self):
        cart = "UGSXO-1999,HWKAM-9680"
        total_discount = compute_discount(
            self.discount_bundles, self.products_list, cart
        )
        self.assertEqual(total_discount, 46.77)


if __name__ == "__main__":
    unittest.main()
