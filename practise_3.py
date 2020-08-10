print("hello")
name = input("what is you name ---> ")
qus =input(f'{name} are you hungry---> ')
qus = qus.lower()

if qus == "yes":
    print("eat first and study")
elif qus == "no":
    print("alright then study")
else :
    print("give me a proper answer")
