def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    while i < len(s):
        if not s[i].islower():
            print(s[i])
        i += 1
    return 
print(main('okkOKO'))