def get_recipe_price(prices, optionals=None, **args):
    if optionals is None:
        optionals = []
    sum_payment = 0
    for ingredient, price_for_100g in prices.items():
        if ingredient not in optionals:
            if args.get(ingredient) is None:
                print(f"Must receive the amount of grams you want to purchase from {ingredient}")
                return None
            sum_payment += args[ingredient] / 100 * price_for_100g
    print(sum_payment)
