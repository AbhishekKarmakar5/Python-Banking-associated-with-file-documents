

class bank_account:
  def __init__(self,balance):
    self.balance=balance
  def withdraw(self,amount):
    if(amount>self.balance):
      self.balance-=amount
      print("The money withdraw is :  Rs.", amount)
      print("The current balance is : Rs.", self.balance)
      return(self.balance)
  def deposit(self,amount):
    self.balance+=amount
    print("The money deposited is :  Rs.", amount)
    print("The current balance is : Rs.", self.balance)
    return(self.balance)


def details(v):
  print("Welcome Client Long Time after Mr. ")
  with open('all_names.txt','r') as f:
    data=f.readlines() 
  print(data[v])


class check:
  def __init__(self):
    pass
  def checking(self):
    flag=0
    t=-1
    num1=int(input("Enter the Bank accont number : "))
    num2=int(input("Enter the Bank Identification ID : "))
    
    with open('acc.txt','r') as f:
      for line in f:
        t+=1
        if (num1==int(line)):
          flag=1
          break
          
    with open('pin.txt','r') as ff:
      for line in ff:
        if (num2==int(line)):
          flag=2
          break
          

    if(flag==2):
      return t
    else:
      return -1


def create(name,n):
  print("Your Account name in Karmakar Bank is : ",name)
  num=0
  for i in range(4):
    num=num*10 + random.randint(0,10)

  print("Your current bank account number is : **** **** ", num)
  with open('acc.txt','a') as f2:
    f2.write(str(num) + '\n')

  with open('ak.txt','a') as wf:
    wf.write(str(n))
    wf.write(".")
    wf.write("      ")
    wf.write(str(name))
    wf.write("\t\t\t**** **** ")
    wf.write(str(num)+'\n')

  num=0
  for i in range(4):
    num=num*10 + random.randint(0,10)

  print("Your Identification ID is : ", num)
  with open('pin.txt','a') as f1:
    f1.write(str(num) + '\n')


import os
def first():
  import os
  
  print('''
      ***********************************************************
      *                                                         *
      *                  WELCOME TO THE                         *
      *                                                         *
      *          | /                                            *
      *          |/                                             *
      *          |\                                             *
      *          | \ARMAKAR SAVINGS BANK                        *                 
      *                                                         *
      *                                                         *
      *                        --Get more than what you want    *                             
      ***********************************************************

      Enter the choice for the following in the bank account:
      1. Have a look at all the account holders name.
      2. Create a new Bank account.
      3. View Balance.
      4. Deposite Cash.
      5. Withdraw Money.
      6. EXIT
    ''')


import random
import os
from time import sleep

acc_id=[]
bank_acc_no=[]

def fun(n):

  n+=1
  first()

  d=int(input())
  if(d==1):
    
    from time import sleep
    
    print("SI.NO.   ACCOUNT HOLDER'S NAME      ACCOUNT NO.")
    print("____________________________________________________")
    with open('ak.txt','r') as rf:
      for line in rf:
        print(line, end='')

    sleep(3)
    
    from time import sleep
    import sys

    for i in range(21):
      sys.stdout.write('\r')
      # the exact output you're looking for:
      sys.stdout.write("[%-20s] %d%%" % (':'*i, 5*i))
      sys.stdout.flush()
      sleep(0.25)
    
    fun(n-1)

  elif(d==2):
    
    name=input("Enter the name : ")
    with open('all_names.txt','a') as wf:
      wf.write(name + '\n')
    with open('bal.txt','a') as bf:
      bf.write("0" + '\n')

    create(name,n)
    sleep(3)
    fun(n)
   

  elif(d==3):
    
    obj=check()
    v=obj.checking()
    if(v>-1):
      details(v)
      with open('bal.txt','r') as bf:
        data=bf.readlines()
      print("Anyway your current balance is : ", data[v])

    else:
      print("--------------------------------------------------")
      print("          The person isn't a card holder")
      print("            Please create a new account")
    
    n-=1
    sleep(3)
    fun(n-1)

  elif(d==4):
    
    obj=check()
    v=obj.checking()
    if(v>-1):
      with open('bal.txt','r') as bf:
        f_cont=bf.readlines()
      obj1=bank_account(f_cont[v])
      bl=obj1.deposit(input("Enter the money to be deposited"))

      k=0
      fo=open('bal.txt','r')
      for line in range(v-1):
        pass
      k=fo.tell
      fo.close()


      with open('bal.txt','w') as wf:
        wf.seek(k)
      f.write(bl)

    else:
      print("--------------------------------------------------")
      print("          The person isn't a card holder")
      print("            Please create a new account")

    n-=1
    sleep(3)
    fun(n)
    
  elif(d==5):
    
    obj=check()
    v=obj.checking()

    if(v>-1):
      with open('bal.txt','r') as bf:
        f_cont=bf.readlines()
      obj1=bank_account(f_cont[v])
      bl=obj1.withdraw(input("Enter the money to be deposited"))

      k=0
      fo=open('bal.txt','r')
      for line in range(v-1):
        pass
      k=fo.tell
      fo.close()
           
      with open('bal.txt','w') as wf:
        wf.seek(k)
      f.write(bl)

    else:
      print("--------------------------------------------------")
      print("          The person isn't a card holder")
      print("            Please create a new account")

    n-=1
    sleep(3)
    fun(n)

  elif(d==6):
    
    print('''
      ********  \     /  
         *       \   /
         *        \ /
         *         /    

         FOR USING KARMAKAR BANK

      ALWAYS READY FOR FUTURE USE 

            MUST VISIT US
      ''')
    exit(0)

  elif (d > 6):
    print("Invalid Input")
    fun(n)

fun(4)

