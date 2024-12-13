def popular_words(text: str, words: list) -> dict:
    text = text.replace("\n", " ")
    text_list = text.split(" ")

    word_count = {}
    for word in words:
        word_count[word] = 0
    
    for text_word in text_list:
        if text_word.lower() in words:
            current = word_count[text_word.lower()]
            word_count[text_word.lower()] = current + 1
    return word_count


print("Example:")
print(
    popular_words(
        """
When I was One
I had just begun
When I was Two
I was nearly new
""",
        ["i", "was", "three", "near"],
    )
)

assert popular_words(
    "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}

print("The mission is done! Click 'Check Solution' to earn rewards!")
