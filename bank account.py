class Bank_Account:
	def __init__(self,accno,name,bal):
		self.accno=int(input("Enter the num:"))
		self.name=input("Enter the Name:")
		self.bal=int(input("Enter the balance:"))
	print("-----\\\\\\WELCOME TO INDIAN BANK/////-----")
	def deposit(self):
		amount=int(input("Enter amount to be Deposited: "))
		self.bal += amount
		
	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		self.bal=amount
		print("\n You Withdrew:", amount)
	def showbal(self):
		print("\n Net Available Balance=",self.bal)
l=[]
print('1.create account\n2.withdraw\n3.deposit\n4.show balance\n5.exit\n')
while True:
	n=int(input('enter the choice:'))
	if n==1:
		x=Bank_Account(1,'name',100)
		l.append(x)
	elif n==2:
		accno1=int(input('enter the account no:'))
		for i in l:
			if i.accno==accno1:
				i.withdraw() 
				break
		else:
				print('Account not found')
	elif n==3:
		accno1=int(input('enter the account no:'))
		for i in l:
			if i.accno==accno1:
				i.deposit()
				break
		else:
				print('account not found')
	elif n==4:
		accno1=int(input('enter the account no:'))
		for i in l:
			if i.accno==accno1:
				i.showbal()
				break
		else:
				print('Account not found')
	elif n==5:
		print('Finish')
		break

