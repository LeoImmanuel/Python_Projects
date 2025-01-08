def sum_to_target(nums_list, target):
    seen = set()
    pairs = set()
    for num in nums_list:
        remainder = target - num
        if remainder in seen:
            pairs.add((min(remainder,num), max(remainder,num)))
        seen.add(num)

    return list(pairs)

print(sum_to_target([2,4,3,7,1,5], 6))

#output: [(2,4),(1,5)]