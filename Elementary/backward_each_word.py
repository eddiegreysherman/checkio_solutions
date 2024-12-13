def backward_string_by_word(text: str) -> str:
    #words = text.split()
    #result = ""
    #for word in words:
    #    result += word[::-1]
    #print(result)
    chars = [char for char in text]
    for char in chars:
        print(char)
    return ""


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
