"""
On 1000g of meat

Nitrite salt: 10g
Salt: 15g
Spices: 0,5g
Monosaccharides: 5g

2 days on every 500g of meat
"""


def nitrite_salt(weight):

    try:
        weight = int(weight)
    except ValueError:
        return 0
    return int(10 * weight/1000)
