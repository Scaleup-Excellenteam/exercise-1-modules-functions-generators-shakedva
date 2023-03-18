def get_recipe_price(prices, optionals=None, **kwargs):
    """
    :param prices: a mapping between ingredients to prices for 100 gram
    :param optionals: list of ingredients that won't be included in the purchase
    :param kwargs: additional arguments of ingredients and the amounts in grams to purchase
    :return: final payment
    """
    if optionals is None:
        optionals = []
    sum_payment = 0
    for ingredient, price_for_100g in prices.items():
        if ingredient not in optionals:
            if kwargs.get(ingredient) is None:
                print(f"Must receive the amount of grams you want to purchase from {ingredient}")
                return None
            sum_payment += kwargs[ingredient] / 100 * price_for_100g
    return sum_payment
