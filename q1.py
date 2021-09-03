
def split(string):
    list=[]
    i = 0
    a=' '
    while i < len(string):
        if string[i]==' ':
            list.append(a)
            a=' '
        else:
            a+=string[i]
            if i == len(string)-1:
                list.append(a)
        i = i + 1
    return list
print(split("my name is nikita sharma"))
