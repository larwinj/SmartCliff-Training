def apply_discount(total, coupon_code):
    discounts = {
        "DISCOUNT10": 0.10,
        "SAVE20": 0.20
    }
    if coupon_code in discounts:
        discount_amount = total * discounts[coupon_code]
        return discount_amount
    return 0
