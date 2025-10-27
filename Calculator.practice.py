with open("calculator_history.txt","w")as file:
    file.write("Calculator History\n \n")


while True:
    Calculator = input("Do you want to perform calculation?  \n 1. Yes \n 2. No \n").lower()
    if(Calculator =="yes"or Calculator =="1"):
        a = float(input("Enter value of A :"))
        b = float(input("Enter value of B :"))
        operation =input("\n 1. + \n 2. - \n 3. * \n 4. / \n")
        if(operation == "+"or operation == "1"):
            c = a+b
            print("Result :",c)
            with open("calculator_history.txt","a")as file:
                    file.write(f"{a}{operation}{b} = {c}\n")
        elif(operation == "-"or operation == "2"):
            c = a-b
            print("Result :",c)
            with open("calculator_history.txt","a")as file:
                    file.write(f"{a}{operation}{b} = {c}\n")
        elif(operation == "*"or operation == "3"):
            c = a*b
            print("Result :",c)
            with open("calculator_history.txt","a")as file:
                    file.write(f"{a}{operation}{b} = {c}\n")
        elif(operation == "/"or operation == "4"):
            if b == 0:
                print("Cannot be divided by Zero.")
                continue
            else:
                c = a/b
                print("Result :",c)
                with open("calculator_history.txt","a")as file:
                    file.write(f"{a}{operation}{b} = {c}\n")
    elif(Calculator =="no"or Calculator =="2"):
        break
    else:
        print("Invalid Input.")
    
    
while True:
    History = input("Do you want to see your History? \n1. Yes \n2. No\n").lower()
    if(History == "1"or History == "yes"):
        with open("calculator_history.txt","r")as file:
            history = file.read()
            print(history)
        break
    elif(History == "2"or History == "no"):
        break
    else:
        print("Invalid Input.")
        


while True:
    History_delete = input("Do you want to Delete your Calculator History? \n1. Yes\n2. No\n").lower()
    if(History_delete == "yes"or History_delete == "1"):
        with open("calculator_history.txt","w")as file:
            file.write("Calculator History deleted successfully.")
        print("Calculator History deleted successfully.")
        break
    elif(History_delete == "no"or History_delete == "2"):
        break
    else:
        print("Invalid Input.")
