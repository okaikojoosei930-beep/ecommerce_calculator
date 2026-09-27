from ecommerce_calculator import (
    calculate_total,
    calculate_discount,
    calculate_shipping,
    calculate_final_price,
    calculate_profit
)


print("Total:", calculate_total(50, 3))

print("Discount:", calculate_discount(200, 10))

print("With shipping:", calculate_shipping(200, 20))

print("Final price:", calculate_final_price(200, 2, 10, 20))

print("Profit:", calculate_profit(100, 60, 5))