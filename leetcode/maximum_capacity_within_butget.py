def max_capacity_in_budget(costs,capacity,budget):
#select atmost two machines strictly less than budget with max capacity returning from the funuction
    count = 0
    output = 0
    while count<2 and budget > 1:
        max_cap = max(capacity)
        cost = costs[capacity.index(max_cap)]
        if cost < budget:
            budget = budget - cost
            output += max_cap
            count += 1
            capacity.pop(capacity.index(max_cap))
        else:
            capacity.pop(capacity.index(max_cap))
    return output


print(max_capacity_in_budget( costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8)) 