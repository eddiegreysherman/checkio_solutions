def is_family(tree):
    source = tree[0][0]
    fam = {}
    for i in range(len(tree)):
        if tree[i][0] not in fam.keys():
            fam.update({tree[i][0]: []})
        if tree[i][0] in fam.keys():
            children = fam.get(tree[i][0])
            children.append(tree[i][1])
            fam[tree[i][0]] = children


    # build a list of all children and fathers
    children = []
    fathers = [n for n in fam.keys()]
    for father in fathers:
        for i in range(len(fam.get(father))):
            children.append(fam[father][i])

    # find the source
    for father in fathers:
        if father not in children:
                source = father

    for father in fathers:
        if father in fam[father]:
            return False  # cannot be your own father!

        for i in range(len(fam[father])):
            if fam[father][i] in fathers:
                if fam[fam[father][i]][0] == father:
                    return False  # you cannot be your fathers father.
                
        if father != source:
            if father in fam[source]:
                for i in range(len(fam[father])):
                    if fam[father][i] in fam[source]:
                        return False  # cannot be a father to your brother

        if father not in children and father != source:
            return False  # No strangers in the family...

    return True


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
        ["Logan", "William"],
        ["William", "Jack"],
        ["Jack", "Mike"],
        ["Mike", "Alexander"]]) == True
    #
    assert is_family([["Logan","Mike"],["Alexander","Jack"],["Jack","Alexander"]]) == False

    assert is_family([["Logan","Mike"],["Alexander","Jack"],["Jack","Logan"]]) == True

    print("Looks like you know everything. It is time for 'Check'!")