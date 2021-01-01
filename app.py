num1 = float(input("1st: "))
num2 = float(input("2nd: "))
operator = input("(M)ultiply (D)ivide (A)dd (S)ubtract  ")
if operator.upper() == "M":
    answer = num1 * num2
    print(f"The anwer is {answer} enjoy your calculation")
elif operator.upper() == "D":
    answer = num1 / num2
    print(f"The anwer is {answer} enjoy your calculation")
elif operator.upper() == "A":
    answer = num1 + num2
    print(f"The anwer is {answer} enjoy your calculation")
elif operator.upper() == "S":
    answer = num1 - num2
    print(f"The anwer is {answer} enjoy your calculation")
else:
    print("Try Again")
