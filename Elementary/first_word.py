def first_word(text: str) -> str:
    words = text.split()
    result = ""
    for word in words:
        if word != " " and word != "...":
            result = word.rstrip(',').split('.')[0]
            print(result)
            break
    return result


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word('Hello.World') == 'Hello'

print("The mission is done! Click 'Check Solution' to earn rewards!")
