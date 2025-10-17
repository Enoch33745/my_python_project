from mod import auto_gene
try:
    while True:
        print("HELLO, WELCOME. CREATE A PASSWORD TO LOGIN TO YOUR INFORMATION")
        psn = int(input("How long do you want your password to be? "))
        print("Would you like to create your own password by yourself or you would want it to be generated" )
        ans = str(input("reply with (auto generate) for it to be generated and (manual) for it to create it yourself "))
        a = auto_gene(psn)

        if ans.lower() == "manual":
            man_pas = print(input("Enter your password "))
            print(f'This is the password you created: {man_pas}')
        elif ans.lower() == "auto generate":
            print(f'This is your auto generated password: {a}')
            
            name = str(input("Enter your name: "))
            age = int(input("How old are your? "))
            home_town = str(input("What's the name of your hometown? "))
            region = str(input("Which region is your hometown located in? "))
            name_of_school = str(input("What's the name of your school? "))
            break 

    while True:
        print("HELLO, PLEASE ENTER YOUR VALID CREDIENTIALS TO ACCESS YOUR INFORMATION")
        psch = input("Enter you password: ")
        if psch == a or man_pas:
            print("LOGIN SUCCESFUL")
            print(f'Your name is {name} and you are {age} years old. The name of your hometown is {home_town} and it is located in {region}.The name of the school you attended is {name_of_school}')
            break
        else:
            print("LOGIN UNSUCCESFUL, PLEASE TRY ENTERING YOUR PASSWORD")
            continue
except(ValueError):
    print("Sorry wrong input, enter the valid type of characters for each answer")

  





# print(f'Your name is, {name} and you are {age} years old. The name of your hometown is {home_town} and it is located in {region}.The name of the school you attended is {name_of_school}')



