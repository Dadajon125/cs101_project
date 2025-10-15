print("--- Triangle Pattern Printer ---")

a = int(input("Enter the desired height of the triangle: "))
for i in range(1, a+1):         
    for j in range(i):           
        print("*", end=" ")
    print()        