import math

sum = 0

#1.Input
x1 = input("Enter: ")
x2 = input("Enter: ")
x3 = input("Enter: ")
op = input("Enter operation: ")


#2.Process
if op == "+":
    sum = int(x1) + sum(x2)
elif op == "-":
    sum = int(x1) - sum(x2)
elif op == "*":
    sum = int(x1) * sum(x2)
elif op == "/":
    sum = int(x1) / sum(x2)
elif op == "avg":
    sum = {int(x1) + sum(x2)}/2
elif op == "sd":
    average = (int(x1) + int(x2) + int(x3))/3
    step1 = int(x1) - average
    step2 = int(x2) - average
    step3 = int(x3) - average
    step4 = (step1**2) + (step2**2) + (step3**2)
    sd = math.sqrt(step4/3)

#3. Output
print(f"Sum: {sum}")
print(f"Sum: {sum}")
print(f"Sum: {sum}")
print(f"Sum: {sum}")
print(f"Sum: {sum}")
print(f"Sum: {sd}")