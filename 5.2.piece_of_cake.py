UNIT = 100


def get_recipe_price(prices, optionals=None, **amount_to_purchase):
    """
    :param prices: a mapping between ingredients to prices for 100 gram
    :param optionals: list of ingredients that won't be included in the purchase
    :param amount_to_purchase: additional arguments of ingredients and the amounts in grams to purchase
    :return: final payment
    """
    if optionals is None:
        optionals = []
    sum_payment = sum([
        (amount_to_purchase.get(ingredient, 0) / UNIT * prices[ingredient])
        for ingredient in prices if ingredient not in optionals
    ])
    return sum_payment


def main():
    """
    Calls the function get_recipe_price with the relevant data and prints its results.
    """
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))


if __name__ == "__main__":
    main()
