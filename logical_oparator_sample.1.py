name = input("enter your phone.number ---> " )
if len(name) < 2:
    print("Name must be at least 3 characters.")
elif len(name) > 14:
    print("name can be a maximum of 10 characters")
else :
    print("number looks good")

