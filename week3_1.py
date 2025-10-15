print("---Movie Ticket Pricer---")
a = int(input("please enter your age: " ))
if a <= 12:

    print("your ticket price is: $8")
elif 13<=a<=64:

    print ("you fall into the 'Adult' category") 
    print("your ticket price is: $10")
else:
    print("you fall into the 'Adult' category")
    print("your ticket price is: $15")