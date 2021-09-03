def palindrome(t):
    a=list(t)
    b=[]
    i=1
    while i<=len(t):
        print(a[-i])
        b.append(a[-i])
        i=i+1
    if b==a:
        print("palindrom")
    else:
        print("not palindrom")
palindrome("mom")