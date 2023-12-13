# importing stuff
import os
import random
import json
# json stuff
# Dictionary mapping rank IDs to roles
rank_roles = {
    1: "Owner",
    2: "Co-Owner",
    3: "Loyalty Palace",
    4: "Ultra Coder",
    5: "Head of FBI",
    6: "FBI",
    7: "Head of Security",
    8: "Security"
}

# Read the JSON file
with open('json/memberRanks.json') as file:
    data = json.load(file)

# Prepare a dictionary to store members according to their ranks
members_by_rank = {}
for member_id, member_info in data.items():
    rank_id = member_info['rankID']
    name = member_info['name']
    role = rank_roles.get(rank_id, f"Rank ID: {rank_id}")  # If a rank ID is not in the mapping, display its ID
    if rank_id not in members_by_rank:
         members_by_rank[rank_id] = []
    members_by_rank[rank_id].append(f"{name}")

# more json stuff
with open('json/alliedCompanies.json') as companies_file:
    companies_data = json.load(companies_file)

# Extract the companies from the data
allied_companies = companies_data.get('companies', [])
# even more json stuff
def is_admin(name):
    with open('json/memberRanks.json') as file:
        data = json.load(file)

    for member_id, member_info in data.items():
        if member_info['name'] == name:
             return True
    return False

# variables
admin = False
running_command = False

# code
def process_action(number):
    os.system("clear")
    global running_command
    running_command = True
    # 1st action
    if number == "1":
         for rank_id, members in members_by_rank.items():
            if members:  # Check if there are members for the role
                role = rank_roles.get(rank_id, f"Rank ID: {rank_id}")
                print(f"{role}: {', '.join(members)}")
    # 2nd action
    elif number == "2":
        print("Description:")
        print("Idk what it is yet")
    # 3rd action
    elif number == "3":
        for company in allied_companies:
           print(company)
    elif number == "4":
        print("https://github.com/LizardRush/ohio-airlines-python-website")
    elif number == "5":
        print("replit.com/@lizardlock1223")
    elif number == "6":
        print("")
    elif number == "7" and admin:
        chosen = random.randint(1, 3)
        if chosen == 1:
            print("chosen 1")
    else:
        print("Command Is Not Defined")
    running_command = False

# welcome line
print("Welcome To The Ohio Airlines Python Website")
print("This Python Website Is Made By Lizard Rush (Edgar)")
# name login
name = input("What is your name: ")
if is_admin(name):
    userinputpin = input("It seems like you are signing in with the name of an admin, enter your admin access pin: ")
    if userinputpin == os.getenv("ADMIN_PIN"):
         admin = True

while True:
	if not running_command:
		input("press enter/return to continue")
		os.system("clear")
		print("action pane for", name)
		print("ohio airlines info")
		print("1: view roles with members")
		print("2: view description")
		print("3: view allied companies")
		print("this python code you're on right now")
		print("4: open GitHub Repository")
		print("5: open lizard rush's replit account (lizardlock1223)")
		print("6: open lizard rush's github account")
		print("ohio airlines")
		if admin:
			print("admin commands")
			print("7: minigame randomizer")
		userinput = input("Input the number of the action: ")
		process_action(userinput)
