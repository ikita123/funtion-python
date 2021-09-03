def calculator(number_1,number_2,oprator):
    if oprator=="+":
        return number_1+number_2
    elif oprator=="-":
        return number_1-number_2
    elif oprator=="*":
        return number_1*number_2
    elif oprator=="%":
        return number_1%number_2
    elif oprator =="/":
        return number_1/number_2
sum_1=calculator(20, 20,"+")
print(sum_1)
