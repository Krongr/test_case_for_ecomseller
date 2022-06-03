import requests
import json


class OzonApi:
    def __init__(self, config):
        self.api_url = 'https://api-seller.ozon.ru/v1/'
        self.headers = {
            'Content-Type': 'application/json',
            'Client-Id': config['ozon_auth']['Client-Id'],
            'Api-key': config['ozon_auth']['Api-key'],
        }

    def promotions_list(self) -> list:
        url = f'{self.api_url}actions'
        return requests.get(url, headers=self.headers).json()

    def products_promotion_list(self, promotion_id, limit=100, offset=0,
                                url_segment='candidates') -> list:
        """url_segment parameter defines wich API method will be used.
        'candidates' will return products that can participate
        in the promotion.
        'products' will return products that are already participating
        in promotions.
        """
        url = f'{self.api_url}actions/{url_segment}'
        data = {
            'action_id': promotion_id,
            'limit': limit,
            'offset': offset,
        }
        return requests.post(url, data=json.dumps(data),
                             headers=self.headers).json()

    def add_product_to_promotion(self, products_for_promotion: list):
        url = f'{self.api_url}actions/products/activate'
        data = products_for_promotion
        return requests.post(url, data=json.dumps(data),
                             headers=self.headers).json()

    def remove_products_from_promotion(self, promotion_id,
                                       products_ids: list):
        url = f'{self.api_url}actions/products/deactivate'
        data = {
            "action_id": promotion_id,
            "product_ids": products_ids,
        }
        return requests.post(url, data=json.dumps(data),
                             headers=self.headers).json()
