class Bank:
    minbal=100
    interest=0.54
    def __init__(self,name,phoneno,aadhar,email,bal,pin):
        self.name=name
        self.phno=phoneno
        self.aadhar=aadhar
        self.email=email
        self.bal=bal
        self.pin=pin
    def Details(self):
        print(f'Name       = {self.name}')
        print(f'Balance    = {self.bal}')
        print(f'PhoneNo    = {self.phno}')
        print(f'AadharCard = {self.aadhar}')
        print(f'E-mail     = {self.email}')
    def enter_pin(self):
        password=int(input())
        return password
    def CheckBal(self):
        count=3
        while count>0:
            print(f"Number of chances you have : {count}")
            print('Enter the 4 digit pin : ')
            if self.enter_pin()==self.pin:
                print(f'Available balance : {self.bal}')
                break
            else:
                print('invalid pin')
                print('Try again')
                count-=1
        else:
            print('You have no chances left')
    def Deposite(self):
        count=3
        while count>0:
            print(f'Number of chances available : {count}')
            print('Enter the 4 digit pin : ')
            if self.enter_pin()==self.pin:
                amount=int(input('Enter the amount to deposite : '))
                if amount%100==0:
                    self.bal+=amount
                    print('Amount Credited Successfull...')
                    break
                else:
                    print('Enter valid Denomination')
            else:
                print('invalid pin')
                print('try again')
                count-=1
        else:
            print('No chances left')
    def withdraw(self):
        count=3
        while count>0:
            print(f'Number of chances Available : {count}')
            print('Enter the 4 digit pin : ')
            if self.enter_pin()==self.pin:
                amount=int(input('Enter amount to withdraw : '))
                if self.minbal<=amount<=amount:
                    if amount%100==0:
                        self.bal-=amount
                        print(f'Amount withdraw successfully completed...')
                        break
                    else:
                        print('Enter valid denomination')
                else:
                    print('invalid limit')
            else:
                print('invalid pin')
                print('try again')
                count-=1
        else:
            print('No chances left')
    def ChangePin(self):
        count=3
        while count>0:
            print(f'Number of chances available : {count}')
            print('Enter the previous 4 digit pin : ')
            pwd=self.enter_pin()
            if len(str(pwd))==len(str(self.pin)):
                if self.enter_pin()==self.pin:
                    password=int(input('Enter the New 4 digit Pin :'))
                    con_Pwd=int(input('Enter the 4 digit pin once again to confirm : '))
                    if password==con_Pwd:
                        print('Password changed successfully...')
                        break
                    else:
                        print('Invalid confirmation password')
                else:
                    print('Invalid pin,Try again..!')
                    count-=1
            else:
                print('Please enter 4 digit pin...  ')
                
        else:
            print('No Chances Left')
        

            
cust1= Bank(name='Kesava',phoneno=9632587410,aadhar=1234567890,email='Kesava@gmail.com',bal=50000,pin=8328)
cust2=Bank('Reddy',2589417630,142536789054,'Reddy@gmail.com',20000,1234)


while True:
    print("""
1 for Deposite
2 for withdraw
3 for CheckBal
4 for ChangePin
""")
    choice=int(input("Enter your choice : "))
    break
