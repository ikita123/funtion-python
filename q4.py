def beautifuldays(i,j,k):
    count=1
    for x in range(i,j+1):
        rx=int(str(x)[::-1])
        if abs(x-rx)%k==0:
            count+=1
    return count
