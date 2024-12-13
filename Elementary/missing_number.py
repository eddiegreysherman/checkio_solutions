def missing_number(items: list[int]) -> int:
    items.sort()
    step_list = []
    index = 0
    step = 0

    for i in range(0, len(items) - 1):
        step_list.append(items[i + 1] - items[i])

    for i in range(0, len(step_list) - 1):
        if step_list[i] > step_list[i - 1]:
            index = step_list.index(step_list[i])
            step = step_list[i - 1] # set the step amount to the value prior to the index of the missing number
    #print(f"The missing number is {items[index] + step}")

    return items[index] + step


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
