
while True:
    org = int(input(" [01]Jam \n [02]Menha \n [03]Zarb \n [04]Taqsim \n [05]Tavan2 \n [06]Tavan3 \n [00]Exit \n >>> Enter a Number : "))
    if org == 1:
        a = float (input("Enter First Number >>> "))
        b = float (input("Enter Second Number >>> "))
        print("Javab = ",a+b)
    elif org == 2:
        a = float (input("Enter First Number >>> "))
        b = float (input("Enter Second Number >>> "))
        print("Javab = ",a-b)
    elif org == 3:
        a = float (input("Enter First Number >>> "))
        b = float (input("Enter Second Number >>> "))
        print("Javab = ",a*b)
    elif org == 4:
        a = float (input("Enter First Number >>> "))
        b = float (input("Enter Second Number >>> "))
        print("Javab = ",a/b)
    elif org == 5:
        a = float(input("Enter a Number : "))
        print("Javab = ",a*a)
    elif org == 6:
        a = float(input("Enter a Number : "))
        print("Javab = ",a*a*a)
    elif org == 0:
        print("Ok By")
        break
    else:
        print("Error 404 !!!")
        break