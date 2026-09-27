def calculate_total(price, quantity):
    """Calculate the total price of products."""
    return price * quantity


def calculate_discount(total, discount_percentage):
    """Calculate the discount amount."""
    return total * (discount_percentage / 100)


def calculate_shipping(total, shipping_cost):
    """Add shipping cost to the order."""
    return total + shipping_cost


def calculate_final_price(price, quantity, discount_percentage=0, shipping_cost=0):
    """Calculate the final price of an order."""
    total = calculate_total(price, quantity)
    discount = calculate_discount(total, discount_percentage)
    discounted_total = total - discount
    final_price = discounted_total + shipping_cost

    return final_price


def calculate_profit(selling_price, cost_price, quantity):
    """Calculate profit from selling products."""
    total_sales = selling_price * quantity
    total_cost = cost_price * quantity

    return total_sales - total_cost