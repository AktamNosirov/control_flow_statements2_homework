def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n%10
   
    n=n//10
    b=n%10
    
    n=n//10
    c=n%10
    
    n=n//10
    d=n%10
    
    n=n//10
    e=n%10
    
    maximum=a
    if  maximum<a :
        maximum=a
    if  maximum<b :
        maximum=b
    if  maximum<c :
        maximum=c
    if  maximum<d :
        maximum=d
    if  maximum<e :
        maximum=e
    return maximum
print(main(12795))








        

        
  