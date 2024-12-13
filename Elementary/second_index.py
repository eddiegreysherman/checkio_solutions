def second_index(text: str, symbol: str) -> int | None:
    index_num = 0
    for i in range(0, len(text)):
        if text[i] == symbol and index_num <= 2:
            index_num += 1
        if index_num == 2:
            return i

    if index_num < 2:
        return None
    


print("Example:")
print(second_index("sims", "s"))

# These "asserts" are used for self-checking
assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
