def changing_direction(elements: list[int]) -> int:
    changes = 0
    direction = None

    for i in range(1, len(elements)):
        # Ascending
        if elements[i] > elements[i - 1]:
            if direction == "desc":
                changes += 1
            direction = "asc"
        elif elements[i] < elements[i - 1]:
            if direction == "asc":
                changes += 1
            direction = "desc"
    return changes


print("Example:")
print(changing_direction([1, 2, 2, 1, 2, 2]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([1, 2, 2, 1, 2, 1, 2]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")