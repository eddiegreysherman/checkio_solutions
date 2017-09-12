from math import pi, acos


def sss(a,b,c):
    degree = pi / 180
    assert a + b > c and b + c > a and c + a > b
    A = acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = acos((c**2 + a**2 - b**2) / (2 * c * a))
    C = 180 - (A/degree) - (B/degree)
    return A/degree, B/degree, C


def checkio(a, b, c):
    try:
        A, B, C = sss(a, b, c)
        result = [
            round(A),
            round(B),
            round(C)]
        return sorted(result)
    except:
        return [0, 0, 0]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(5, 4, 3) == [37, 53, 90]