# https://www.codewars.com/kata/595910299197d929a10005ae
def pizza_rewards(customers, min_orders, min_price):
    # initialize set of eligible customers
    eligible_customers = set()
    
    for customer, orders in customers.items():
        order_count = 0
        # count eligible orders
        for order in orders:
            if order >= min_price:
                order_count += 1
        
        if order_count >= min_orders:
            eligible_customers.add(customer)
            
    return eligible_customers
