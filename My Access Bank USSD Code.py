print("Here are the available USSD Code")
print("Access:*901#")
def menu():
	print("You have enter USSD Code for", bank)
	print("1>Check balance\n2>Transfer\n3>Airtime\n")
	option=eval(input("Select an option:"))
	if(option==1):
		pin=eval(input("enter your four digit pin:\n"))
		print("(0097777690-N10000.58) NAME: MUHAMMAD ABDULLAHI)")
		print("Transaction Sucessful")
		back=eval(input("1>To return to menu\n2>To exit\n"))
		if(back==1):
			menu()
		elif(back==2):
			exit()
		else:
			("wrong input")
	elif(option==2):
		account=eval(input("Enter reciepient ACCOUNT NUMBER:\n"))
		amount=eval(input("Enter Transfer Amount\n"))
		print(f"Transfer N{amount} to MUHAMMAD ABDULLAHI")
		pin=eval(input("Enter your four digit pin:\n"))
		print("Transaction Succeful")
		back=eval(input("1>To return to menu\n2>To exit\n"))
		if(back==1):
			menu()
		elif(back==2):
			exit()
		else:
			("wrong input")
	elif(option ==3):
		airtime=eval(input("1>self\n2>Others\n"))
		if(airtime==1):
			amount=eval(input("Enter amount\n"))
			pin=eval(input("Enter your four daigit pin\n"))
			print("Transaction Successful")
			back=eval(input("1>To return to menu\n2>To Cancle\n"))
			back=eval(input("1>To return to menu\n2>To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")
		if(airtime==2):
			number=eval(input("Enter Number\n"))
			amount=eval(input("Enter amount\n"))
			pin=eval(input("Enter your four daigit pin\n"))
			print("Transaction Successful")
			back=eval(input("1>To return to menu\n2>To Cancle\n"))
			back=eval(input("1>To return to menu\n2>To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")			
ussd=eval(input("please enter your USSD Code:"))
if(ussd==901):
	bank="Access Bank"
	menu()
else:
	("wrong input")