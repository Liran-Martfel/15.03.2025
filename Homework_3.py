nums = [4, -2, 0, 7, -5, 3]
from pprint import pprint
# -> {
#     "positive": [4,7,3],
#     "negative": [-2,-5],
#     "zero": [0]
# }

def group_numbers(nums: list) -> dict:
    '''
    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    numbers = {
#           key   : value
        'positive': [],
        'negative': [],
        'zero': []
    }
    for num in nums:
        if num > 0:
            #adding the number to the value 'num' with the key 'positive'
            numbers['positive'].append(num)
        elif num < 0:
            #adding the number to the value 'num' with the key 'negative'
            numbers['negative'].append(num)
        elif num == 0:
            #adding the number to the value '0' with the key 'zero'
            numbers['zero'].append(num)
    return numbers

pprint(group_numbers(nums))