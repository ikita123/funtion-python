def pagecount(n,p):
    f=p//2
    if n%2==1:
        b=(n-p)//2
    else:
        b=(n-p+1)//2
    return min(f,b)