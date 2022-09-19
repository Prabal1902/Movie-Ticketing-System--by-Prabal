import pandas as pd
import matplotlib.pyplot as plt
import csv
import random

def admin_prompt():
    print("===================================================================")
    print("Greetings ADMIN")
    print("What would you like to do")
    print("*******************************************************************")
    print("(1) see movie list")
    print("(2) access customer list")
    print("(3) access customer wallet")
    print("(4) access performance graphs")
    print("(5) Quit")
    print("\n")
    return

def admin_cprompt():
    adc = int(input(">>>>>"))
    if adc == 1:
        c= input("What would you like to do? (R for read , E for edit, B to go back) >>>")
        if c in ['r', 'R', 'read', 'READ', 'Read'] :
            df = pd.read_csv('movie list.csv')
            print(df)
        elif c in ['e', 'E', 'EDIT', 'Edit', 'edit']:
            print("\n") #\n is for line break
            print('*Please NOTE!*')
            print('*to add a column , simply type its name in the "Column name" option*')
            print('*and assign its designated row in the "row number" option*')
            print('*To delete entire rows or colums , edit each selected cell manually to avoid accidental data removal*')
            print('*You cannot delete multiple/entire rows or columns in one go*')
            print("\n") #\n is for line break
            df = pd.read_csv("movie list.csv")
            column = input("Column name--->")
            row = int(input("row number--->"))
            new = input("edit---->")
            # updating the column value/data
            df.loc[row, column] = new
            # writing into the file
            df.to_csv("movie list.csv")
            print(df)
        elif c in ['b','B','back','Back','BACK']:
            admin_prompt()


    elif adc == 2 :
        c = input("What would you like to do? (R for read , E for edit, B to go back) >>>")
        if c in ['r', 'R', 'read', 'READ', 'Read']:
            df = pd.read_csv('customer table.csv')
            print(df)
        elif c in ['e', 'E', 'EDIT', 'Edit', 'edit']:
            print("\n")
            print('*Please NOTE!*')
            print('*to add a column , simply type its name the "Column name" option.*')
            print('*and assign its designated row in the "row number" option*')
            print("\n")
            df = pd.read_csv("customer list.csv")
            column = input("Column name--->")
            row = int(input("row no.---."))
            new = input("edit---->")
            # updating the column value/data
            df.loc[row, column] = new
            # writing into the file
            df.to_csv("customer list.csv")
            print(df)
        elif c in ['b', 'B', 'back', 'Back', 'BACK']:
            admin_prompt()


    elif adc == 3 :
        c = input("What would you like to do? (R for read , E for edit, B to go back) >>>")
        if c in ['r', 'R', 'read', 'READ', 'Read']:
            df = pd.read_csv('user wallet.csv')
            print(df)
        elif c in ['e', 'E', 'EDIT', 'Edit', 'edit']:
            print("\n")
            print('*Please NOTE!*')
            print('*to add a column , simply type its name the "Column name" option.*')
            print('*and assign its designated row in the "row number" option*')
            print("\n")
            df = pd.read_csv("user wallet.csv")
            column = input("Column name--->")
            row = int(input("row no.---."))
            new = input("edit---->")
            # updating the column value/data
            df.loc[row, column] = new
            # writing into the file
            df.to_csv("user wallet.csv")
            print(df)
        elif c in ['b', 'B', 'back', 'Back', 'BACK']:
            admin_prompt()

    elif adc == 4 :
        col_list = ["Name", "rating"]
        df = pd.read_csv("movie list.csv", usecols=col_list)
        x = df["Name"]
        y = df["rating"]
        plt.bar(x, y, color='b', width=0.72, label="ratings")
        plt.xlabel('Names of Movies')
        plt.ylabel('Ratings')
        plt.title('Performance of Movies')
        plt.legend()
        plt.show()

    elif adc == 5 :
        quit()

    admin_prompt()
    admin_cprompt()


def greetings():
    print('----------GREETINGS!----------')
    print('-----welcome to P&R Pictures!-----')
    print('Please register with email and password!!')
    print("\n")
    print('Have you already registered?')
    print('type 1 for YES')
    print('type 0 for NO')
    print('To log into ADMIN please enter your ADMIN CODE')
    print("\n")
greetings()


def greet_log():
    cs = int(input('your answer---->'))
    if cs == 1:
        print("\n")
        print("~~~~~WELCOME BACK!~~~~~")
        print("\n")


    if cs == 0:
        print("-----PLEASE REGISTER-----")
        print("\n")
    if cs == 1925 or cs == 42069:
        print("\n")
        def Aregister():
            with open("admin table.csv", mode="a", newline="") as f:
                print('****ADMIN REGISTRATION PAGE****')
                writer = csv.writer(f, delimiter=",")
                id = input('ID:')
                password = input('Password:')
                password2 = input('re-enter password:')
                if password == password2:
                    writer.writerow([id, password])
                    print('registration is succesful!')
                    print("\n")
                    print('GREETINGS ADMIN!')
                    print('****LOG-IN****')
                else:
                    print('please try again.')
                    Aregister()

        def Alogin():
            id = input('ID:')
            password = input('enter password:')
            with open("admin table.csv", mode="r") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    if row == [id, password]:
                        print("\n")
                        print("*****Log in succesful!*****")
                        print("*****you are logged in!*****")
                        print("\n")
                        return True
            print('Please try again!')
            return False

        Aregister()
        flag=Alogin()
        admin_prompt()
        admin_cprompt()
greet_log()


def register():
    with open("customer table.csv", mode="a", newline="") as f:
       print('****REGISTRATION****')
       writer = csv.writer(f,delimiter=",")
       email = input('email:')
       password = input('Password:')
       password2= input('re-enter password:')
       if password == password2:
          writer.writerow([email,password])
          print("\n")
          print('registration is succesful!')
          print('THANK YOU FOR REGISTERING AS A CUSTOMER IN RAWAT PICTURES!')
          print('KINDLY LOG IN TO CONTINUE!')
          print("\n")
          print('****LOG-IN****')
       else:
          print('please try again.')
          register()


def login():
    email = input('enter email:')
    password = input('enter password:')
    with open("customer table.csv", mode="r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if row == [email,password]:
                print("\n")
                print("*****Log in succesful!*****")
                print("*****you are logged in!*****")
                print("\n")
                return True
    print('Please try again!')
    return False

register()
login()

def c_prompt():
    print("\n")
    print('=====================================================================')
    print("Welcome to Rawat Pictures!")
    print("\n")
    print("To check the list of movies avaiable in our theater , press 1")
    print("To check your wallet  , press 2")
    print("To exit , press 3")
    print("\n")

def a_prompt():
    choice = int(input("YOUR CHOICE:"))
    print("\n")
    if choice == 1:
        df = pd.read_csv('movie list.csv')
        print(df)
        print('==============================')
        select = int(input('Enter the MOVIE No you wish to book:'))
        n = random.random()
        print("\n")
        print('Booking succesful. CODE-', n)
        print("\n")
        rate = int(input("Please consider rating the movie, out of 10 [1 being WORST and 10 being BEST!]"))
        df = pd.read_csv("movie list.csv")
        df.loc[select, 'rating'] = rate
        df.to_csv("movie list.csv", index=False)
        print(df)

    elif choice == 2:
        print('Please Note!')
        print('You cannot add,change or edit your user wallet.')
        print('Please go to the reception and request to enter money in your user wallet')
        print('We will let management update your wallet records')
        print('\n')
        df = pd.read_csv('user wallet.csv')
        print(df)

    elif choice == 3:
        quit()

    c_prompt()
    a_prompt()

c_prompt()
a_prompt()










