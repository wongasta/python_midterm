import pprint
pp = pprint.PrettyPrinter(indent=4)

#input
from utilities.vowels_counting import count_vowels
bags = [{
    'sku': 1234,
    'brand': 'LV',
    'color': 'brown',
    'texture': 'weird',
    'price': 1000
},{
    'sku': 4234,
    'brand': 'Coach',
    'color': 'black',
    'texture': 'leather',
    'price': 20
},{
    'sku': 1235,
    'brand': 'Chanel',
    'color': 'yellow',
    'texture': 'nasty',
    'price': 4000
},{
    'sku': 1134,
    'brand': 'YSL',
    'color': 'white',
    'texture': 'smoothie',
    'price': 1100
},{
    'sku': 4532,
    'brand': 'LV',
    'color': 'black',
    'texture': 'ruggity',
    'price': 500
}]

shoes = [{
    'sku': 1402,
    'brand': 'Steven Madam',
    'color': 'pink',
    'price': 10,
},{
    'sku': 1042,
    'brand': 'Celine',
    'color': 'white',
    'price': 4000
}]


def get_sku(i):
    return i['sku']

bag_skus = map(get_sku, bags)
#print(list(bag_skus))

shoes_skus = map(get_sku, shoes)
#print(list(shoes_skus))

def get_discount(i):
    i['sales_price'] = i['price']*0.8
    return i

bags_with_discount = list(map(get_discount, bags))
print(bags_with_discount)

shoes_with_discount = list(map(get_discount, shoes))
#print(shoes_with_discount)

price_limit = 1000


def filter_price(i):
    is_within_price_range = i['price'] < price_limit
    return is_within_price_range

bags_within_price_range = list(filter(filter_price, bags))
#print(bags_within_price_range)

shoes_within_price_range = list(filter(filter_price, shoes))
#print(shoes_within_price_range)

def filter_discounted_price(i):
    is_within_price_range = i['sales_price'] < price_limit
    return is_within_price_range

discount_bags_within_price_range = list(filter(filter_discounted_price, map(get_discount, bags)))
print(discount_bags_within_price_range)

