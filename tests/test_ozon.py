import unittest
import configparser
from api.ozon import OzonApi


config = configparser.ConfigParser()
config.read("settings.ini")

tester = OzonApi(config)


class TestApiMethods(unittest.TestCase):
    def test_promotions_list(self):
        self.assertIsInstance(tester.promotions_list(), dict)

    def test_products_promotion_list(self):
        promotion_id = tester.promotions_list()['result']
        id = promotion_id[0]
        test_object = tester.products_promotion_list(promotion_id=id)
        self.assertIsInstance(test_object, dict)
