A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A > B and A > C:
    print("A is bigger")
elif B > A and B > C:
    print("B is bigger")
else:
    print("C is bigger")