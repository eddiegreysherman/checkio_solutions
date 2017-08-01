import operator

def checkio(text):
    c_dict = {}
    for c in text:
        if c.isalpha():
            c_dict.update({c.lower(): text.count(c)})

    sorted_list = sorted(c_dict.items(), key=operator.itemgetter(1))
    #print(sorted_dict[-1:][0][1])
    # Find all keys with values = to the largest.
    match_list = []
    for s in sorted_list:
        if s[1] == sorted_list[-1:][0][1]:
            match_list.append(s[0])

    match_list.sort()

    return match_list[0]
    #return 'a'

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