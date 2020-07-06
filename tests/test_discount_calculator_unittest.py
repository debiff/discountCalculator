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

    def test_six_products_without_bundle_match(self):
        cart = "BMZZN-7122,OVVUK-8951,OWHEM-6595,HWYZJ-0056,FTGBE-9666,MOWIB-2747"
        total_discount = compute_discount(
            self.discount_bundles, self.products_list, cart
        )
        self.assertEqual(total_discount, 21.07)

    def test_no_bundle_match(self):
        cart = "LNIAL-8393,JSVVX-8355,EAZKL-0112,EAZKL-0112"
        total_discount = compute_discount(
            self.discount_bundles, self.products_list, cart
        )
        self.assertEqual(total_discount, 0)

    def test_bundle_composed_from_same_element(self):
        cart = "AQKQX-3571,FAWCD-2035"
        total_discount = compute_discount(
            self.discount_bundles, self.products_list, cart
        )
        self.assertEqual(total_discount, 83.18)

    def test_same_products_match_more_than_one_bundle(self):
        cart = "FAWCD-2035,RIMYD-0243,VYVLA-7385"
        total_discount = compute_discount(
            self.discount_bundles, self.products_list, cart
        )
        self.assertEqual(total_discount, 44.35)


if __name__ == "__main__":
    unittest.main()
