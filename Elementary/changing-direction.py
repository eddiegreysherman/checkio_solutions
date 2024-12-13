def changing_direction(elements: list[int]) -> int:
    changes = 0
    direction = "asc"
    for i in range(0, len(elements) - 1):
        if i == 0:
            continue
        if (elements[i] >= elements[i - 1]):
            # no change was made, going up
            # if prior changes we need to check
            if changes != 0:
                if (elements[i] > elements[i - 1]) or (elements[i] < elements[i - 1]):
                    changes += 1
            continue
        if (elements[i] < elements[i - 1]):
            #there was a change so count it
            changes += 1
    return changes


print("Example:")
print(changing_direction([1, 2, 3, 2, 1]))

# These "asserts" are used for self-checking
#assert changing_direction([1, 2, 3, 4, 5]) == 0
#assert changing_direction([1, 2, 3, 2, 1]) == 1
#assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
#assert changing_direction([1, 2, 2, 1, 2, 1, 2]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")