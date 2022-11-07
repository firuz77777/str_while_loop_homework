def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c = 0
    i = 0
    while i < len(s):
        if not s[i].isdigit() and not s[i].isalpha():
            c = c + 1
        i = i + 1
    return c 
print(main('dicj;;s'))