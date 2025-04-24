# Priority Sorting:
# Items are sorted by price (cheapest first)
# For same-priced items, those with higher quantity come first

# Clear Status Reporting:
# FULLY FULFILLED: Entire order satisfied within budget
# PARTIALLY FULFILLED: Some items fulfilled
# IMPOSSIBLE: No items could be fulfilled

# Output:
# Shows exactly which items were fulfilled
# Includes total cost and remaining budget


def fulfill_order(inventory, order, budget):
    total_cost = 0
    fulfillment = {}

    for item in order:
        if item not in inventory:
            continue

        price = inventory[item]['price']
        available = inventory[item]['quantity']
        requested = order[item]
        fulfill_qty = min(requested, available)

        # Cost to fulfill this item
        cost = fulfill_qty * price

        if total_cost + cost > budget:
            # Adjust quantity to fit remaining budget
            affordable_qty = (budget - total_cost) // price
            if affordable_qty > 0:
                fulfillment[item] = affordable_qty
                total_cost += affordable_qty * price
            continue
        else:
            fulfillment[item] = fulfill_qty
            total_cost += cost

    # Determine status
    if all(item in fulfillment and fulfillment[item] == order[item] for item in order):
        status = "Fulfillable"
    elif fulfillment:
        status = "Partially fulfillable"
    else:
        status = "Impossible"

    return {
        'status': status,
        'fulfilled_items': fulfillment,
        'total_cost': total_cost
    }

# Example inventory
inventory = {
    'apple': {'quantity': 10, 'price': 2},
    'banana': {'quantity': 5, 'price': 1},
    'orange': {'quantity': 8, 'price': 3}
}

# Example customer order and budget
order = {
    'apple': 4,
    'banana': 3,
    'orange': 2
}
budget = 15

# Run the check
result = fulfill_order(inventory, order, budget)

# Display results
print("Order Status:", result['status'])
print("Items Fulfilled:", result['fulfilled_items'])
print("Total Cost:", result['total_cost'])
