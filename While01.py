def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    while a < len(s):
        q = print(s[a])
        a = a + 1
    return q
print(main('unolplpl'))