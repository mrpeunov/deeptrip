def get_min_max_price(tours):
    min_price = 1000000000
    max_price = 0
    for tour in tours:
        if tour.price > max_price:
            max_price = tour.price

        if tour.price < min_price:
            min_price = tour.price

    return min_price, max_price
