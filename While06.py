def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a = 0
    i = 0
    while i < len(s):
        if s[i] == 'a':
            a += 1
        if s[i] == 'e':
            a += 1
        if s[i] == 'i':
            a += 1
        if s[i] == 'o':
            a += 1 
        if s[i] == 'u':
            a += 1
        else :
            a += 0
        i += 1
    return a