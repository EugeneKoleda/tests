"""
On 1000g of meat

Nitrite salt: 10g
Salt: 15g
Spices: 0,5g
Monosaccharides: 5g

2 days on every 500g of meat
"""


def return_nitrite_salt(weight):
    """This function get weight of meat and return weight of nitrite salt"""

    try:
        weight = int(weight)
    except ValueError:
        return 0
    return int(10 * weight/1000)


def return_salt(weight):
    """This function get weight of meat and return weight of salt"""

    try:
        weight = int(weight)
    except ValueError:
        return 0
    return int(15 * weight / 1000)


def return_spices(weight):
    """This function get weight of meat and return weight of spices"""

    try:
        weight = int(weight)
    except ValueError:
        return 0
    return float(0.5 * weight / 1000)


def return_monosaccharides(weight):
    """This function get weight of meat and return weight of monosaccharides"""

    try:
        weight = int(weight)
    except ValueError:
        return 0
    return int(5 * weight / 1000)


def return_days(weight):
    """This function get weight of meat and return the amount of days until ready"""

    try:
        weight = int(weight)
    except ValueError:
        return 0
    return int(2 * weight / 1000)

