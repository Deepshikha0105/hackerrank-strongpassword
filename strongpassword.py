def minimumNumber(n, password):
    count=0
    a=0
    b=0
    c=0
    d=0
    l="!@#$%^&*()-+"
    

    for i in password:

        if i.isupper():
            a=1
        elif i.islower():
            b=1
        elif i.isdigit():
            c=1
        else:
            d=1
            
            
    if n>6:
        e=a+b+c+d
        count=4-(a+b+c+d)
    
    else:
        count1=n+(4-(a+b+c+d))
        if count1<7:
            count=(6-count1)+(4-(a+b+c+d))
        else:
            count=(4-(a+b+c+d))
            
            
        
    return (count)
