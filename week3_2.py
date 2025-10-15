print("--- Running Total Calculator ---")
print("Enter numbers to add them up. Type 'done' to see the total.")
a = "done"
c = 0
while a == "done" :
    b = input("Enter a number or 'done':")
    if b == "done" :
        print ("--- Final Calculation ---")
        break
    c+=float (b)
    print(f"Current total : {c:.1f}") 
print (f"The final sum of all numbers is: {c:.1f}")

