first = int(input("Enter first num: "))
second = int(input("Enter second num: "))
third = int(input("Enter third num: "))

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
