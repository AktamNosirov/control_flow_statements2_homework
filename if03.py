def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """  
    if c>b>a or a>b>c :
        return b
    elif a>c>b or b>c>a :
        return c
    else :
        return a 
print(main(3,6,3))


