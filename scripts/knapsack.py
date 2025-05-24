"""
Problem: 0/1 Knapsack Problem - Find the Best Item Combination

You are preparing for a trip and have a limited-capacity backpack (6 kg).
You have a list of items, each with a weight and a value.
You cannot take more than one of each item (i.e., no repetitions), and your goal is to maximize
the total value of the items you carry without exceeding the weight limit.

Implement a function that determines the optimal combination of items to include in the backpack
so that the total value is as high as possible, and the total weight does not exceed the capacity.

Each item is represented as a dictionary with:
- "name": the name of the item
- "weight": the weight of the item (in kilograms)
- "value": the value or utility score of the item

The function should return:
- the maximum value achievable
- the list of item names that produce this value
"""

water = {"weight": 3, "value": 10, "name": "water"}
book = {"weight": 1, "value": 3, "name": "book"}
food = {"weight": 2, "value": 9, "name": "food"}
jacket = {"weight": 2, "value": 5, "name": "jacket"}
camera = {"weight": 1, "value": 6, "name": "camera"}
items = [water, book, food, jacket, camera]

capacity = 6

def find_best_combination(itemList: list[dict], maxCapacity: int) -> tuple[int, str]:
    # Build the item x weight table
    table = [[{"value": 0, "items": []} for j in range(0, maxCapacity + 1)] for _ in itemList]

    for i, item in enumerate(itemList):
        for j in range(1, maxCapacity + 1):
            item_weight = item["weight"]
            item_name = item["name"]
            item_value = item["value"]

            if i == 0:
                if item_weight <= j:
                    table[i][j]["value"] = item_value
                    table[i][j]["items"] = [item_name]
                continue

            total_value = 0
            combined_items = []
            if item_weight <= j:
                # Check the best value from remaining capacity and add current item's value
                remaining_capacity = j - item_weight
                total_value = table[i-1][remaining_capacity]["value"] + item_value
                combined_items = table[i-1][remaining_capacity]["items"].copy() + [item_name]

            cell = {}
            previous_cell = table[i-1][j]
            if previous_cell.get("value", 0) > total_value:
                cell["value"] = previous_cell["value"]
                cell["items"] = previous_cell["items"].copy()
            else:
                cell["value"] = total_value
                cell["items"] = combined_items
            table[i][j] = cell

    # After building the table, get the result from the last cell
    best = table[-1][-1]
    return best["value"], ",".join(best["items"])

# Call the function and print the result
value, selected_items = find_best_combination(items, capacity)
print("The best result reached " + str(value) + " points with the items: " + selected_items)
