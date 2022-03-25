def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if c>b>a or c>a>b :
        return c
    if b>a>c or b>c>a :
        return b
    if a>b>c or a>c>b :
        return a
print(main(1,5,2))
