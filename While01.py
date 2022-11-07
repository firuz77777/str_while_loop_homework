def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c=0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            c+=1
        i = i + 1
    return c
print(main('ertdf6gybj23'))
# s = 'start'
# i = 0
# while i < len(s):
#     print(s[i])
#     i = i + 1
