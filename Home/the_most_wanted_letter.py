import operator


def checkio(text):
    c_dict = {}
    # convert all characters to lowercase
    text = text.lower()
    for c in text:
        if c.isalpha():
            c_dict.update({c: text.count(c)})

    sorted_list = sorted(c_dict.items(), key=operator.itemgetter(1))

    # Find all keys with values matching the largest.
    # sorted_list[-1:][0][1] - gives you the largest value
    # build a new list match_list with keys = to that value
    match_list = []
    for s in sorted_list:
        if s[1] == sorted_list[-1:][0][1]:
            match_list.append(s[0])

    # sort the keys in alphabetical order
    match_list.sort()
    # return the first key in the sorted list
    return match_list[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")