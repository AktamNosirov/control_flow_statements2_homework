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
    if a>c>b or b>c>a :
        return c
    if b>a>c or c>a>b :
        return a 
print(main(5,7,1))
