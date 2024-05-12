from tkinter import *
import tkinter.font as tfont
import sqlite3
import random
from datetime import datetime
from re import match, search, compile
from tkcalendar import DateEntry
t = Tk()
t.geometry("500x500")
t.resizable(0, 0)
fontStyle = tfont.Font(family="Impact", size=15)

a = StringVar()
b = StringVar()
c = IntVar()
d = StringVar()
x = StringVar()
f = IntVar()
fn = StringVar()
ln = StringVar()
Em = StringVar()
ph = IntVar()
da = StringVar()
ba = IntVar()
at = StringVar()
dan = IntVar()
dam = IntVar()
wan = IntVar()
wam = IntVar()
san = IntVar()
ram = IntVar()
tam = IntVar()
tif = StringVar()
cb = IntVar()
th = IntVar()

kr = 1
global_function = None
global_function2 = None
global_function3 = None
global_function4 = None
global_function5 = None
global_function6 = None

def home():
    f0 = Frame(bg="blue")
    f0.place(x=0, y=0, width=500, height=500)

    # Creating a label with a welcome message on the blue frame
    u0 = Label(f0, text="Online Banking System", fg="white", bg="blue", font=fontStyle)
    u0.place(x=120, y=50)

    # Creating a "Sign Up" button that, when clicked, will call the Signup function
    b0 = Button(f0, text="Login Here", command=Login)
    b0.place(x=130, y=80, width=100, height=30)

    # Creating a "Sign In" button that, when clicked, will call the signin function
    b1 = Button(f0, text="Register Here", command=signin)
    b1.place(x=260, y=80, width=100, height=30)


def Login():
    # Create a blue-colored frame for the login window
    f1 = Frame(bg="blue")
    f1.place(x=0, y=0, width=500, height=500)

    # Label for the welcome message
    u1 = Label(f1, text="Welcome to User Authentication", fg="white", bg="blue", font=fontStyle)
    u1.place(x=120, y=50)

    # Button to go back to the home screen
    b2 = Button(f1, text="Home", command=home)
    b2.place(x=0, y=0, width=110, height=40)

    # Label and Entry for the user's Phone number
    u3 = Label(f1, text="Email:", fg="white", bg="blue")
    u3.place(x=90, y=160)

    e1 = Entry(f1, font=("Impact", 10), textvariable=a)
    e1.place(x=260, y=160, width=120)

    # Label and Entry for the user's email
    u4 = Label(f1, text="Password:", fg="white", bg="blue")
    u4.place(x=90, y=190)

    e2 = Entry(f1, font=("Impact", 10), show="*", textvariable=b)
    e2.place(x=260, y=190, width=120)

    b3 = Button(f1, text="Login", command=loginVarification)
    b3.place(x=175, y=250, width=100, height=30)
    
    
    u26 = Label(f1, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=450)

    u26 = Label(f1, text="", fg="white", bg="blue")
    u26.place(x=90, y=450)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message

def createAccount():
    f4 = Frame(bg="blue")
    f4.place(x=0, y=0, width=500, height=500)

    # Label for the welcome back message
    u15 = Label(f4, text="Welcome to joining this Bank (❁´◡`❁)", fg="white", bg="blue", font=fontStyle)
    u15.place(x=90, y=80)

    b5 = Button(f4, text="Back", command=loginVarification)
    b5.place(x=0, y=0, width=110, height=40)

    u16 = Label(f4, text="First name:", fg="white", bg="blue")
    u16.place(x=90, y=160)

    e1 = Entry(f4, font=("Impact", 10), textvariable=fn)
    e1.place(x=260, y=160, width=120)

    u17 = Label(f4, text="Last name:", fg="white", bg="blue")
    u17.place(x=90, y=190)

    e2 = Entry(f4, font=("Impact", 10), textvariable=ln)
    e2.place(x=260, y=190, width=120)

    u18 = Label(f4, text="Email:", fg="white", bg="blue")
    u18.place(x=90, y=220)

    e3 = Entry(f4, font=("Impact", 10), textvariable=Em)
    e3.place(x=260, y=220, width=120)

    u19 = Label(f4, text="Phone Number:", fg="white", bg="blue")
    u19.place(x=90, y=260)

    e4 = Entry(f4, font=("Impact", 10), textvariable=ph)
    e4.place(x=260, y=260, width=120)

    u20 = Label(f4, text="Date of Birth(YYYY-MM-DD):", fg="white", bg="blue")
    u20.place(x=90, y=290)

    e5 = DateEntry(f4, font=("Impact", 10), textvariable=da, date_pattern='yyyy-mm-dd')
    e5.place(x=260, y=290, width=120)



    u21 = Label(f4, text="Balance:", fg="white", bg="blue")
    u21.place(x=90, y=320)

    e6 = Entry(f4, font=("Impact", 10), textvariable=ba)
    e6.place(x=260, y=320, width=120)

    u22 = Label(f4, text="Account Type:(saving, current)", fg="white", bg="blue")
    u22.place(x=90, y=360)

    e7 = Entry(f4, font=("Impact", 10), textvariable=at)
    e7.place(x=260, y=360, width=120)

    b3 = Button(f4, text="create", command=data_i_CreateAccTab)
    b3.place(x=175, y=400, width=100, height=30)




    u26 = Label(f4, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=450)

    u26 = Label(f4, text="", fg="white", bg="blue")
    u26.place(x=90, y=450)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message
    

def data_i_CreateAccTab():
    un = []

    def AccountNoVarification(fnn, lnn, Emm, phh, daa, baa, att, current_date):
        try:
            # Connect to the SQLite database
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            # Execute a SELECT query to retrieve user data based on the email
            select_query = "SELECT AccountNo FROM create_account"
            cursor.execute(select_query)
            all_account_numbers = cursor.fetchall()
            flat_listt = [int(item[0]) for item in all_account_numbers]

            def randamNo():
                five_digit_number = random.randint(10000, 99999)
                return five_digit_number

            n = randamNo()
            un.append(n)
            while True:
                if (n) in flat_listt:
                    un.clear()
                    randamNo()
                else:
                    un.append(n)
                    break
            cursor.execute(f"INSERT INTO create_account (Fname,Lname,Email,PhoneNo,DateOfBirth,AccountNo,Balance,AccountType,Date) VALUES('{fnn}', '{lnn}', '{Emm}', {phh}, '{daa}', {n}, {baa}, '{att}', '{current_date}')")
            connection.commit()
            print("account sucessfully created...")
            print(f"your account number is : {n}")
            global_function("Account successfully created. Your account number is: {}".format(n), color="white")
        except Exception as e:
            print(f"Error: {e}")
            global_function("Error: {}".format(e), color="red")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
    current_date = datetime.now().date()
    try:
        fnn = fn.get()
        lnn = ln.get()
        Emm = Em.get()
        phh = ph.get()
        daa = da.get()
        baa = ba.get()
        att = at.get()
        phh = int(phh)
        phh = str(phh)
        daa = str(daa)
    
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        ma = match(email_pattern, Emm)
        phone_pattern = r'^(\+91-?)?([6-9]\d{9})$'
        matp = match(phone_pattern, phh)
        dob_pattern = r'^(?!0000)(?:(?!02-(30|31))\d{4}-(0[13-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])|(?!02-29)\d{4}-02-(0[1-9]|1[0-9]|2[0-8])|(?!02-(30|31))\d{4}-02-29)$'
        matdob = match(dob_pattern, daa) and daa <= str(current_date)
        if bool(ma):
            if bool(matp):
                if bool(matdob):
                    try:
                        if att in ['saving', 'current']:
                            AccountNoVarification(fnn, lnn, Emm, phh, daa, baa, att, current_date)
                        else:
                            global_function("inter valid account type!", color='red')
                    except:
                        print("enter a numbers only!")
                        global_function("enter a numbers only!", color="red")
                else:
                    print("invalid date of birth!")
                    global_function("invalid date of birth!", color="red")
            else:
                print("invalid phone number!")
                global_function("invalid phone number!", color="red")
        else:
            print("invalid email! ")
            global_function("invalid email! ", color="red")

        
    except:
        print("Something is Wrong!!!")
        global_function("Something is Wrong!!!", color="red")

def loginVarification():
    lem = a.get()
    lpa = b.get()
    def get_user_data(email, pasword):
        try:
            # Connect to the SQLite database
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            # Execute a SELECT query to retrieve user data based on the email
            select_query = f"SELECT * FROM Login WHERE Email = '{email}'"
            cursor.execute(select_query)

            # Fetch the result (assuming there is only one matching record)
            user_data = cursor.fetchone()

            if user_data:
                # Extract values from the result
                s_no, fetched_email, fetched_password, fetched_PhoneNo = user_data


                if lem == fetched_email:
                    if lpa == fetched_password:
                    
                        f3 = Frame(bg="blue")
                        f3.place(x=0, y=0, width=500, height=500)

                        # Label for the welcome back message
                        u11 = Label(f3, text="***** welcome to Dhakad Bank *****", fg="white", bg="blue", font=fontStyle)
                        u11.place(x=90, y=80)

                        # Button to go back to the home screen
                        b5 = Button(f3, text="Logout", command=home)
                        b5.place(x=0, y=0, width=110, height=40)

                        b6 = Button(f3, text="create account", command=createAccount)
                        b6.place(x=70, y=170, width=110, height=40)

                        b6 = Button(f3, text="deposit", command=deposit)
                        b6.place(x=200, y=170, width=110, height=40)

                        b6 = Button(f3, text="withdraw", command=withdraw)
                        b6.place(x=330, y=170, width=110, height=40)

                        b6 = Button(f3, text="Transfer", command=transfer)
                        b6.place(x=70, y=250, width=110, height=40)

                        b6 = Button(f3, text="check balance", command=checkB)
                        b6.place(x=200, y=250, width=110, height=40)

                        b6 = Button(f3, text="Transaction History", command=history)
                        b6.place(x=330, y=250, width=110, height=40)

                    else:
                        print("Wrong Password!")
                        global_function("Wrong Password!", color='red')
            else:
                print("Wrong email!:")
                global_function("Wrong email!:", color='red')

        except Exception as e:
            print(f"Error: {e}")
            global_function("Error: {}".format(e), color='red')

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    # Example usage:
    get_user_data(lem, lpa)

def history():
    f9 = Frame(bg="blue")
    f9.place(x=0, y=0, width=500, height=500)

    
    u21 = Label(f9, text="Transaction History....＼(((￣(￣(￣▽￣)￣)￣)))／", fg="white", bg="blue", font=fontStyle)
    u21.place(x=70, y=80)

    b21 = Button(f9, text="Back", command=loginVarification)
    b21.place(x=0, y=0, width=110, height=40)

    u22 = Label(f9, text="Enter Account Number:", fg="white", bg="blue")
    u22.place(x=90, y=160)

    e22 = Entry(f9, font=("Impact", 10), textvariable=th)
    e22.place(x=250, y=160, width=120)

    b7 = Button(f9, text="Check", command=historyyw)
    b7.place(x=190, y=200, width=110, height=40)
    
    u26 = Label(f9, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=300)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message
    
    
   
    u27 = Label(f9, text="", fg="white", bg="blue")
    u27.place(x=90, y=330)
    
    def set_message(message, color="red"):
        u27.config(text=message, fg=color)
        
    global global_function2
    global_function2 = set_message
    
    #
    u28 = Label(f9, text="", fg="white", bg="blue")
    u28.place(x=90, y=360)
    
    def set_message(message, color="red"):
        u28.config(text=message, fg=color)
        
    global global_function3
    global_function3 = set_message
    
    #
    u29 = Label(f9, text="", fg="white", bg="blue")
    u29.place(x=90, y=400)
    
    def set_message(message, color="red"):
        u29.config(text=message, fg=color)
        
    global global_function4
    global_function4 = set_message
    
    #
    u30 = Label(f9, text="", fg="white", bg="blue")
    u30.place(x=90, y=430)
    
    def set_message(message, color="red"):
        u30.config(text=message, fg=color)
        
    global global_function5
    global_function5 = set_message
    
    #
    u31 = Label(f9, text="", fg="white", bg="blue")
    u31.place(x=90, y=450)
    
    def set_message(message, color="red"):
        u31.config(text=message, fg=color)
        
    global global_function6
    global_function6 = set_message

def historyyw():
    try:
        thh = th.get()
        int(thh)
        def get_data_his():
            try:

                
                connection = sqlite3.connect('bank.db')
                cursor = connection.cursor()

                select_query = f"SELECT * FROM Historyy where accountN = {thh}"
                cursor.execute(select_query)
                all_details = cursor.fetchall()
                # print(all_details)

                data = all_details

                # Header
                header = ["sNo", "paid_to", "amount", "received_from", "amount", "date ", "account"]
                formatted_data = []    # [header]

                # Add data rows
                for row in data:
                    formatted_data.append(list(row))
                global_function("|sNo.| paid_to | Amount | Rec_from | Amount | Date | Account |", color='white')
                
                formatted_data.reverse()
                for row in formatted_data:
                    l = []
                    # print([", ".join(map(str, row))])
                    l.append([", ".join(map(str, row))])
                ls = len(formatted_data)                   
                print(ls)
                def case1():
                    global_function2(str(["----".join(map(str, formatted_data[0]))]), color='white')
                def case2():
                    global_function3(str(["----".join(map(str, formatted_data[1]))]), color='white')
                def case3():
                    global_function4(str(["----".join(map(str, formatted_data[2]))]), color='white')
                def case4():
                    global_function5(str(["----".join(map(str, formatted_data[3]))]), color='white')
                def default_case():
                    global_function6(str(["----".join(map(str, formatted_data[4]))]), color='white')
                switch = {1:case1, 2:case2, 3:case3, 4:case4}
                def execute_case(case):
                    switch.get(case, default_case)()
                if ls ==0:
                    print("History not available")   
                    global_function("History not available!!!", color='red') 
                elif ls == 1:
                    execute_case(1)    
                elif ls < 5:  
                    for u in range(1,ls+1):
                        execute_case(u)
                else:
                    for i in range(1,6):
                        execute_case(i)
                   
            except Exception as e:
                 print(f"Error: {e}")
                 print("Account number does not exist, check!!!")
                 global_function("History not available, check!!!", color='red')

            finally:
                # Close the cursor and connection
                cursor.close()
                connection.close()
        get_data_his()
    except Exception as e:
        print("Account number not exist!!!")
        global_function("Account number not exist!!!", color='red')


def checkB():
    f8 = Frame(bg="blue")
    f8.place(x=0, y=0, width=500, height=500)

    # Label for the welcome back message
    u21 = Label(f8, text="Checking your Balance ⚖.........💸", fg="white", bg="blue", font=fontStyle)
    u21.place(x=130, y=80)

    b21 = Button(f8, text="Back", command=loginVarification)
    b21.place(x=0, y=0, width=110, height=40)

    u22 = Label(f8, text="Enter Account Number:", fg="white", bg="blue")
    u22.place(x=90, y=160)

    e22 = Entry(f8, font=("Impact", 10), textvariable=cb)
    e22.place(x=250, y=160, width=120)

    b7 = Button(f8, text="Check", command=checkb)
    b7.place(x=190, y=200, width=110, height=40)
    
    u26 = Label(f8, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=450)

    u26 = Label(f8, text="", fg="white", bg="blue")
    u26.place(x=90, y=450)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message

def checkb():
    try:
        cbb = cb.get()
        int(cbb)
        connection = sqlite3.connect('bank.db')
        cursor = connection.cursor()

        select_query = "SELECT AccountNo FROM create_account"
        cursor.execute(select_query)
        all_account_numbers = cursor.fetchall()

        flat_list = [int(item[0]) for item in all_account_numbers]
        if cbb in flat_list:
             select_queryy = f"SELECT Balance FROM create_account where AccountNo = {cbb}"
             cursor.execute(select_queryy)
             all_Balance = cursor.fetchone()
             flat_b = (all_Balance[0])
             int(flat_b)
             print(flat_b)
             global_function("Balance is : {}".format(flat_b), color='white')
        else:
             print("Account Number does not exist!")
             global_function("Account Number does not exist!", color='red')
    except Exception as e:
        print(f"Account number not exist!!!")
        global_function("Account number not exist!!!", color='red')

def transfer():
    f7 = Frame(bg="blue")
    f7.place(x=0, y=0, width=500, height=500)

    # Label for the welcome back message
    u21 = Label(f7, text="Transfer to... o(*￣▽￣*)o😡", fg="white", bg="blue", font=fontStyle)
    u21.place(x=130, y=80)

    b21 = Button(f7, text="Back", command=loginVarification)
    b21.place(x=0, y=0, width=110, height=40)

    u22 = Label(f7, text="Self Account Number:", fg="white", bg="blue")
    u22.place(x=90, y=160)

    e22 = Entry(f7, font=("Impact", 10), textvariable=san)
    e22.place(x=250, y=160, width=120)

    u23 = Label(f7, text="Receiver account Number:", fg="white", bg="blue")
    u23.place(x=90, y=200)

    e23 = Entry(f7, font=("Impact", 10), textvariable=ram)
    e23.place(x=250, y=200, width=120)

    u23 = Label(f7, text="Enter Amount:", fg="white", bg="blue")
    u23.place(x=90, y=240)

    e23 = Entry(f7, font=("Impact", 10), textvariable=tam)
    e23.place(x=250, y=240, width=120)

    u23 = Label(f7, text="Enter IFSC CODE:", fg="white", bg="blue")
    u23.place(x=90, y=280)

    e23 = Entry(f7, font=("Impact", 10), textvariable=tif)
    e23.place(x=250, y=280, width=120)

    b7 = Button(f7, text="Transfer", command=transferw)
    b7.place(x=190, y=350, width=110, height=40)
    
    u26 = Label(f7, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=450)

    u26 = Label(f7, text="", fg="white", bg="blue")
    u26.place(x=90, y=450)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message

def transferw():
    try:
        sann = san.get()
        ramm = ram.get()
        tamm = tam.get()
        tiff = tif.get()
        dk = int(sann)
        kd = int(ramm)
        try:            
            tm = int(tamm)
        
            # Connect to the SQLite database
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            select_query = "SELECT AccountNo FROM create_account"
            cursor.execute(select_query)
            all_account_numbers = cursor.fetchall()
            select_queryy = f"SELECT Balance FROM create_account where AccountNo = {dk}"
            cursor.execute(select_queryy)
            all_Balance = cursor.fetchone()
            current_date = datetime.now().date()

            print(all_Balance)

            flat_list = [int(item[0]) for item in all_account_numbers]
            flat_b = (all_Balance[0])
            int(flat_b)
            if dk in flat_list:
                if sann != ramm:
                    if flat_b > tamm:
                        if kd in flat_list:
                            select_queryyy = f"SELECT Balance FROM create_account where AccountNo = {ramm}"
                            cursor.execute(select_queryyy)
                            t_Balance = cursor.fetchone()
                            flat_tb = (t_Balance[0])
                            int(flat_tb)
                            
                            tubalance = flat_tb+tamm
                            
                            cursor.execute(f"UPDATE create_account SET Balance = {tubalance} WHERE AccountNo = {ramm}")
                            connection.commit()
                            cursor.execute(f"INSERT INTO Historyy (Paid_to, amountt, Received_from, amount, date, accountN) VALUES({dk}, {0}, {kd}, {tm}, '{current_date}', {kd})")
                            connection.commit()
                        newBalance = int(flat_b - tamm)
                        print(newBalance)
                        def insert_data_tTable(sa, oa, ba, am, da, ifs):
                            insert_query = f"INSERT INTO Transfer (sAccountN, oAccountN, Balancee, amount, date, ifsc_code) VALUES({sa}, {oa}, {ba}, {am}, '{da}', '{ifs}')"
                            cursor.execute(insert_query)
                            connection.commit()
                            cursor.execute(f"INSERT INTO Historyy (Paid_to, amountt, Received_from, amount, date, accountN) VALUES({sa}, {am}, {oa}, {0}, '{da}', {sa})")
                            connection.commit()
                            print("Data inserted successfully")
                            global_function("Transfered successfully...", color='white')
                            cursor.execute(f"UPDATE create_account SET Balance = {newBalance} WHERE AccountNo = {sann}")
                            connection.commit()
                        
                        insert_data_tTable(sann, ramm, newBalance, tamm, current_date, tiff)
                        cursor.close()
                        connection.close()
                    else:
                        print("insufficient balance!")
                        global_function("insufficient balance!", color='red')
                else:
                    print("Both account number cann't be same!")
                    global_function("Both account number cann't be same!", color='red')
            else:
                print("account number not exist")
                global_function("account number not exist", color='red')
        except:
            print("enter numbers only!") 
            global_function("account number not exist!", color='red')  
    except Exception as e:
        print(f"Enter numbers only")
        global_function("account number not exist", color='red')

    finally:
        # Close the cursor and connection
        # cursor.close()
        # connection.close()
        pass


def withdraw():
    f6 = Frame(bg="blue")
    f6.place(x=0, y=0, width=500, height=500)

    # Label for the welcome back message
    u21 = Label(f6, text="Withdraw here ✍️(◔◡◔)", fg="white", bg="blue", font=fontStyle)
    u21.place(x=150, y=80)

    b21 = Button(f6, text="Back", command=loginVarification)
    b21.place(x=0, y=0, width=110, height=40)

    u22 = Label(f6, text="Account Number:", fg="white", bg="blue")
    u22.place(x=90, y=160)

    e22 = Entry(f6, font=("Impact", 10), textvariable=wan)
    e22.place(x=200, y=160, width=120)

    u23 = Label(f6, text="Amount:", fg="white", bg="blue")
    u23.place(x=90, y=200)

    e23 = Entry(f6, font=("Impact", 10), textvariable=wam)
    e23.place(x=200, y=200, width=120)

    b7 = Button(f6, text="Debit", command=withdraww)
    b7.place(x=190, y=250, width=110, height=40)
    
    u26 = Label(f6, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=450)

    u26 = Label(f6, text="", fg="white", bg="blue")
    u26.place(x=90, y=450)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message

def withdraww():
    try:
        wann = wan.get()

        try:
            wamm = wam.get()
            int(wamm)
            
            dk = int(wann)
            # Connect to the SQLite database
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            select_query = "SELECT AccountNo FROM create_account"
            cursor.execute(select_query)
            all_account_numbers = cursor.fetchall()
            select_queryy = f"SELECT Balance FROM create_account where AccountNo = {dk}"
            cursor.execute(select_queryy)
            all_Balance = cursor.fetchone()
            current_date = datetime.now().date()

            print(all_Balance)

            flat_list = [int(item[0]) for item in all_account_numbers]
            flat_b = (all_Balance[0])
            int(flat_b)
            if dk in flat_list:
                if flat_b > wamm:
                    newBalance = int(flat_b - wamm)
                    print(newBalance)
                    def insert_data_wTable(acc, cred, datee, ba):
                        insert_query = f"INSERT INTO withdraw (AccountN, debit, date, Balancee) VALUES({acc}, {cred}, '{datee}', {ba})"
                        cursor.execute(insert_query)
                        connection.commit()
                        cursor.execute(f"INSERT INTO Historyy (Paid_to, amountt, Received_from, amount, date, accountN) VALUES({acc}, {cred}, {acc}, {0}, '{datee}', {acc})")
                        connection.commit()
                        print("Data inserted successfully")
                        global_function("Success ^_-", color='white')
                        cursor.execute(f"UPDATE create_account SET Balance = {newBalance} WHERE AccountNo = {dk}")
                        connection.commit()

                    insert_data_wTable(wann, wamm, current_date, newBalance)
                    cursor.close()
                    connection.close()
                else:
                    print("insufficient balance!")
                    global_function("insufficient balance!", color='red')
            else:
                print("account number not exist")
                global_function("account number not exist", color='red')
        except UnboundLocalError:
            print("enter numbers only!")
            global_function("account number not exist!", color='red')
        except Exception as e:
            print(f"Enter numbers only!")
            global_function("account number not exist!", color='red')
    except UnboundLocalError:
        print("account number not exist!!!")
        global_function("account number not exist!!!", color='red')
    except Exception as e:
        print(f"account number not exist!!!")
        global_function("account number not exist!!!", color='red')

    finally:
        # Close the cursor and connection
        # cursor.close()
        # connection.close()
        pass

def deposit():
    f5 = Frame(bg="blue")
    f5.place(x=0, y=0, width=500, height=500)

    # Label for the welcome back message
    u21 = Label(f5, text="deposit here ✍️(◔◡◔)", fg="white", bg="blue", font=fontStyle)
    u21.place(x=150, y=80)

    b21 = Button(f5, text="Back", command=loginVarification)
    b21.place(x=0, y=0, width=110, height=40)

    u22 = Label(f5, text="Account Number:", fg="white", bg="blue")
    u22.place(x=90, y=160)

    e22 = Entry(f5, font=("Impact", 10), textvariable=dan)
    e22.place(x=200, y=160, width=120)

    u23 = Label(f5, text="Amount:", fg="white", bg="blue")
    u23.place(x=90, y=200)

    e23 = Entry(f5, font=("Impact", 10), textvariable=dam)
    e23.place(x=200, y=200, width=120)

    b7 = Button(f5, text="credit", command=depositw)
    b7.place(x=190, y=250, width=110, height=40)
    
    u26 = Label(f5, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=450)

    u26 = Label(f5, text="", fg="white", bg="blue")
    u26.place(x=90, y=450)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message

def depositw():
    try:
        dann = dan.get()
        damm = dam.get()
        dk = int(dann)
        try:
            int(damm)
            # Connect to the SQLite database
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            select_query = "SELECT AccountNo FROM create_account"
            cursor.execute(select_query)
            all_account_numbers = cursor.fetchall()
            select_queryy = f"SELECT Balance FROM create_account where AccountNo = {dk}"
            cursor.execute(select_queryy)
            all_Balance = cursor.fetchone()
            current_date = datetime.now().date()

            print(all_Balance)

            flat_list = [int(item[0]) for item in all_account_numbers]
            flat_b = (all_Balance[0])

            if dk in flat_list:
                newBalance = int(flat_b + damm)
                print(newBalance)
                def insert_data_deTable(acc, cred, datee, ba):
                    insert_query = f"INSERT INTO deposit (AccountN, credit, date, Balancee) VALUES({acc}, {cred}, '{datee}', {ba})"
                    cursor.execute(insert_query)
                    connection.commit()
                    cursor.execute(f"INSERT INTO Historyy (Paid_to, amountt, Received_from, amount, date, accountN) VALUES({acc}, {0}, {acc}, {cred}, '{datee}', {acc})")
                    connection.commit()
                    print("Data inserted successfully")
                    global_function("Success ^_~", color='white')
                    cursor.execute(f"UPDATE create_account SET Balance = {newBalance} WHERE AccountNo = {dk}")
                    connection.commit()

                insert_data_deTable(dann, damm, current_date, newBalance)
                cursor.close()
                connection.close()
            else:
                print("account number not exist")
                global_function("account number not exist", color='red')
        except:
            print("account number not exist!")
            global_function("account number not exist", color='red')
    except UnboundLocalError:
        print("enter numbers only!")
        global_function("enter numbers only!", color='red')
    except Exception as e:
        print("Enter numbers only!!")
        global_function("enter numbers only!", color='red')

    finally:
        # Close the cursor and connection
        # cursor.close()
        # connection.close()
        pass

def signin():
    # Create a blue-colored frame for the sign-in window
    f2 = Frame(bg="blue")
    f2.place(x=0, y=0, width=500, height=500)

    # Label for the welcome back message
    u6 = Label(f2, text="welcome to Bank, Signin Here", fg="white", bg="blue", font=fontStyle)
    u6.place(x=90, y=80)

    # Label and Entry for the user's username
    u7 = Label(f2, text="Enter your Email:", fg="white", bg="blue")
    u7.place(x=90, y=130)

    e4 = Entry(f2, font=("Impact", 10), textvariable=d)
    e4.place(x=260, y=130, width=120)

    # Label and Entry for the user's password
    u9 = Label(f2, text="Enter your Password:", fg="white", bg="blue")
    u9.place(x=90, y=160)

    e5 = Entry(f2, font=("Impact", 10), textvariable=x)
    e5.place(x=260, y=160, width=120)

    # Label and Entry for the user's Phone number signin
    u10 = Label(f2, text="Phone number:", fg="white", bg="blue")
    u10.place(x=90, y=190)

    e8 = Entry(f2, font=("Impact", 10), textvariable=f)
    e8.place(x=260, y=190, width=120)

    # Button to go back to the home screen
    b4 = Button(f2, text="Home", command=home)
    b4.place(x=0, y=0, width=110, height=40)

    # Button to trigger the sign-in process
    b5 = Button(f2, text="Register", command=SigninRegistration)
    b5.place(x=175, y=220, width=100, height=30)
    
    u26 = Label(f2, text=" ", fg="white", bg="blue")
    u26.place(x=90, y=450)

    u26 = Label(f2, text="", fg="white", bg="blue")
    u26.place(x=90, y=450)

    
    def set_message(message, color="red"):
        u26.config(text=message, fg=color)
        
    global global_function
    global_function = set_message


def SigninRegistration():
    try:
        rd = d.get()
        re = x.get()         
        rf = f.get()
        rf = int(rf)
        rf = str(rf)

        def insert_data(email, password, PhoneNumber):
            try:
                # Connect to the SQLite database
                connection = sqlite3.connect('bank.db')
                cursor = connection.cursor()

                # Insert data into the 'Login' table
                insert_query = f"INSERT INTO Login (Email, pass, Phone) VALUES ('{email}', '{password}', {PhoneNumber})"
                cursor.execute(insert_query)

                # Commit the changes
                connection.commit()
                print("Data inserted successfully")
                global_function("Success  (•_•)", color='white')
                cursor.close()
                connection.close()

            except Exception as l:
                print(f"Error: {l}")
                global_function("Error : {}".format(l), color='red')
            finally:
                # Close the cursor and connection
                # cursor.close()
                # connection.close()
                pass

                # Example usage:

    
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        phone_pattern = r'^(\+91-?)?([6-9]\d{9})$'

        ma = match(email_pattern, rd)
        matchp = match(phone_pattern, rf)

                    
        k = bool(ma)
        r = bool(matchp)
        if k:
            if r:
                insert_data(rd, re, rf)
            else:
                print("enter valid phone number!")
                global_function("enter valid phone number!", color='red')
        else:
              print("invalid Email!")
              global_function("invalid Email!", color='red')
                          
        
    except:
        print("Something is wrong!!!")
        global_function("Something is Wrong!!!", color='red')   

# calling home function
if __name__ == "__main__":
    home()
    t.mainloop()
