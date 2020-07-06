import unittest
import json


class TestDiscountMethod(unittest.TestCase):
    def setUp(self):
        with open("./samples/bundles.json") as f:
            self.discount_bundles = list(json.load(f))

        with open("./samples/products.json") as f:
            self.products_list = list(json.load(f))


if __name__ == "__main__":
    unittest.main()
