# importing required stuff
import os
# code
admin_logged_in = False
running_command = False
def process_action(number):
	running_command = True
	# 1st action
	if number == "1":
		print("Owner: Nixon")
		print("Co-Owner: ???")
		print("Loyalty palace: Cecelia")
		print("Christmas Ultra Programmer: Edgar")
		print("Head of FBI: Kushal")
		print("???: ???")
		print("???: ???")
		print("???: ???")
	# 2nd action
	elif number =="2":
		print("Description:")
		print("Idk what it is yet")
	# 3rd action
	elif number =="3":
		print("Lizard Co.")
		print("Dino Co.")
		print("GimKit Frenzy")
	elif number =="4":
		print("https://github.com/LizardRush/ohio-airlines-python-website")
	elif number =="5":
		print("replit.com/@lizardlock1223")
	elif number =="6":
		print("")
	else:
		print("Command Is Not Defined")
	running_command = False
	print("—————————————————————————————————")
# welcome line
print("Welcome To The Ohio Airlines Python Website")
print("This Python Website Is Made By Lizard Rush (Edgar)")
# name login
name = input("What is your name: ")
if name == "Edgar" or name == "Nixon" or name == "Sebastian" or name == "Cecelia":
	userinputpin = input("it seems like you are signing in with a name of an admin, enter your admin acess pin: ")
	if userinputpin == os.getenv("ADMIN_PIN"):
		admin_logged_in = False
while True:
	if not running_command:
		print("action pane for", name)
		print("ohio airlines info")
		print("1: view roles with members")
		print("2: view description")
		print("3: view allied companies")
		print("this python code you're on right now")
		print("4: open GitHub Repository")
		print("5: open lizard rush's replit account (lizardlock1223)")
		print("6: open lizard rush's github account")
		userinput = input("Input the number of the action: ")
		process_action(userinput)