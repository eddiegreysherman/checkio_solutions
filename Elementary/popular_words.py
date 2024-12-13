def popular_words(text: str, words: list) -> dict:
    word_list = text.split()
    word_and_count = {}
    count = 0
    for word in words:
        for i in range(len(word_list)):
            if word_list[i] == word:
                count += 1
        word_and_count[word] = count


    return word_and_count


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