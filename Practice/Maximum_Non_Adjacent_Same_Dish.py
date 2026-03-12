from collections import defaultdict

def max_non_adjacent_same_dish(dishes):
    positions = defaultdict(list)

    # store indices of each dish
    for i, dish in enumerate(dishes):
        positions[dish].append(i)

    max_count = 0

    for dish in positions:
        idx = positions[dish]
        count = 0
        last_taken = -2

        for i in idx:
            if i != last_taken + 1:
                count += 1
                last_taken = i

        max_count = max(max_count, count)

    return max_count
