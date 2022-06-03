import configparser
from api.ozon import OzonApi


def get_promotion_ids(promotions_list:list)->list:
    promotion_ids = []
    for promotion in promotions_list:
        promotion_ids.append(promotion['id'])
    return promotion_ids


def create_products_for_promotions_list(ozon_api:OzonApi, 
                                        promotion_ids:list)->list:
    products_for_promotions = []
    for promotion in promotion_ids:
        promotion_with_products = {
            'action_id': promotion,
            'products': [],
        }
        for product in ozon_api.products_promotion_list(
            promotion,
            url_segment='candidates',
        )['result']['products']:
            promotion_with_products['products'].append({
                'action_price': product['max_action_price'],
                'product_id': product['id']
            })
        products_for_promotions.append(promotion_with_products)        
    return products_for_promotions



if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("settings.ini")

    ozon_api = OzonApi(config)

    promotions = ozon_api.promotions_list()['result']
    promotion_ids = get_promotion_ids(promotions)
   
    products = create_products_for_promotions_list(ozon_api, promotion_ids)
    
    for position in products:
        print(ozon_api.add_product_to_promotion(position))
