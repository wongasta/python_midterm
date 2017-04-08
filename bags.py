#input
from utilities.vowels_counting import count_vowels
bags = [{
    'sku': 1234,
    'brand': 'LV',
    'color': 'brown',
    'texture': 'weird'
},{
    'sku': 4234,
    'brand': 'Coach',
    'color': 'black',
    'texture': 'leather'
},{
    'sku': 1235,
    'brand': 'Chanel',
    'color': 'yellow',
    'texture': 'nasty'
},{
    'sku': 1134,
    'brand': 'YSL',
    'color': 'white',
    'texture': 'smoothie'
},{
    'sku': 4532,
    'brand': 'LV',
    'color': 'black',
    'texture': 'ruggity'
}]

def main():
    def find_keys_with_vowels(bags, category, num_vowels):
        bags_with_vowels = []
        for bag in bags:
            #total_vowels = count_vowels(bag[category])
            if count_vowels(bag[category])['total_vowel'] >= num_vowels:
                bags_with_vowels.append(bag)
        print(bags_with_vowels)
    find_keys_with_vowels(bags, 'brand', 2)
    find_keys_with_vowels(bags, 'texture', 3)
    find_keys_with_vowels(bags, 'color', 1)
    return
main()


#         vowels_in_texture = ["a", "i", "e", "o", "u"]
#         for bag in bags:
#             if bag['texture'] == ['a' or 'i' or 'e' or 'o' or 'u'] and count_vowels > 2:
#                 texture_bag.append(bag)
#             else:
#                 return("")
#     count_vowels(bag)
# print(texture_bag)





#for bag in bags:
    #print(bag['brand'])


#output - list of unqiue brands in bags
#['LV', 'Chanel', 'YSL']


#brand_name = []
#for bag in bags:
    #brand_name.append(bag['brand'])
#print(set(brand_name))

#black_bag = []
#for bag in bags:
    #    if bag['color'] == 'black':
    #   black_bag.append(bag)
        #print(set(black_bag))
    # else:
#    print("")
#print(black_bag)

#sku_bag = []
#for bag in bags:
    # if bag['sku'] < 4000:
    #sku_bag.append(bag)
    #else:
#   print("")
#print(sku_bag)


# def get_bags_with_vowels(bags):
#     texture_bag = []
#     for bag in bags:
#         total_vowels = count_vowels(bag['texture'])
#         if total_vowels > 2:
#             texture_bag.append(bag)
#
#     print(texture_bag)
#
# get_bags_with_vowels(bags)

# def get_bags_with_vowels(bags):
#     brand_bag = []
#     for bag in bags:
#         total_vowels = count_vowels(bag['brand'])
#         if total_vowels > 1:
#             brand_bag.append(bag)
#     print(brand_bag)
# get_bags_with_vowels(bags)