def addNote(name,age,mobile_no):
  with open('sample.txt','a') as fobj:
    fobj.write(f"name = {name}\nAge = {age}\nMobileNo = {mobile_no}\n--------------------\n")
  print('Contact saved..!')
def readNote():
  try: 
    with open('sample.txt') as fobj:
      data = fobj.read()
      print(data)
  except FileNotFoundError:
    print('No Contacts Found...')


while True:
  print('1.Add Note \n2.Read Note\n3.Exit')
  ch=int(input('Enter your choice : '))
  if ch==1:
    name=input("Enter your name : ")
    age=input("Enter your age : ")
    mobile_no=input("Enter your phone number : ")
    addNote(name,age,mobile_no)
  elif ch==2:
    readNote()
  elif ch==3:
    break
  else:
    print("Invalid Choice...\n ")
  
