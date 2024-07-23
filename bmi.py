while True:
    print("""
            command?
          1) ask ur doubt
          2) exit

""")
    choice = int(input("enter ur command"))

    if choice == 1:
        print("")
        name = input("enter ur name : ")
        weight =int(input("enter ur weight : "))
        height =int(input("enter ur height : "))
        heightmeter =height/100
        bmi = weight/height**2
        if bmi > 18.4 :
            print("under weight")
        elif bmi <18.4 and bmi >24.9 :
            print("normal")
        elif bmi <24.9 and bmi >39.9 :
            print("over weight")
        else:
            print("obese")
    elif choice == 2 :
        print("exited is successfull")
    else:
        print("invalid command")