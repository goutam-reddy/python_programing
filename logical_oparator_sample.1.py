name = input("enter your name ---> " )
if len(name) < 2:
    print("Name must be at least 3 characters.")
elif len(name) > 14:
    print("name can be a maximum of 15 characters")
else :
    print("name looks good")

