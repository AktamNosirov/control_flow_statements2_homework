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
        
    if maximum==a :
       return 1
    if maximum==b :
       return 2
    if maximum==c :
        return 3
    if maximum==d :
       return 4
    if maximum==e :
        return 5
print(main(12983))


