# -------- IMPORTS -------------

import os
from dataclasses import dataclass
from info import cohort_lnames, cohort_fnames, cohort_data, cohort_fullnames
from search import search
from termcolor import colored

# --------- DATACLASS --------------


@dataclass
class Directory:
	screen: str
	user: str


# ----------- KEYS FOR SORTED LISTS --------------


def full_name(mem) -> str:
	return mem.fullname


def co_lname(mem) -> str:
	return mem.lname


def co_fname(mem) -> str:
	return mem.fname


def co_age(mem) -> int:
	return mem.age


# ----------- SORTED LISTS -------------

# Last Names
s_cohort_lname = sorted(cohort_data, key=co_lname)
s_cohort_lnamerev = sorted(cohort_data, key=co_lname, reverse=True)

# First Names
s_cohort_fname = sorted(cohort_data, key=co_fname)
s_cohort_fnamerev = sorted(cohort_data, key=co_fname, reverse=True)

# Age
s_cohort_age = sorted(cohort_data, key=co_age)
s_cohort_agerev = sorted(cohort_data, key=co_age, reverse=True)

# ----------- SORTING FUNCTIONS ------------


# First Name
def sortingbyfirstname(order) -> None:
	print('')
	if order == "Ascending":
		for cohort in s_cohort_fname:
			print(cohort.fname, cohort.lname, sep=" ", end="\n\n")
	elif order == "Descending":
		for cohort in s_cohort_fnamerev:
			print(cohort.fname, cohort.lname, sep=" ", end="\n\n")


# Last Name
def sortingbylastname(order) -> None:
	print('')
	if order == "Ascending":
		for cohort in s_cohort_lname:
			print(cohort.fname, cohort.lname, sep=" ", end="\n\n")
	elif order == "Descending":
		for cohort in s_cohort_lnamerev:
			print(cohort.fname, cohort.lname, sep=" ", end="\n\n")


# Age
def sortingbyage(order) -> None:
	print('')
	if order == "Ascending":
		for cohort in s_cohort_age:
			print(cohort.age, cohort.fname, cohort.lname, sep=" ", end="\n\n")
	elif order == "Descending":
		for cohort in s_cohort_agerev:
			print(cohort.age, cohort.fname, cohort.lname, sep=" ", end="\n\n")


# ========= DIRECTORY SELECTION ===============


def directory_selection(directory: Directory):
	directory.user = directory_input_Helper()
	directory.screen = 'directory'
	if directory.user == "First Name":
		order = ascending_or_descending()
		sortingbyfirstname(order)
	elif directory.user == "Last Name":
		order = ascending_or_descending()
		sortingbylastname(order)
	elif directory.user == "Age":
		order = ascending_or_descending()
		sortingbyage(order)


# --------------- INPUT HELPER FUNCTIONS ---------- #
# Main Screen InputHelper
def inputhelper(directory: Directory, mem) -> bool:
	if directory.user.title() in mem: return True
	elif directory.user.lower() == "directory": return True
	elif directory.user.lower() == "quit": return True
	else: return False


#Ascending/Descending InputHelper
def ascending_or_descending() -> str:
	order = input(
	 "\nWould you like this list to be in [Descending] or [Ascending] order? \n>"
	).title()
	while order != "Ascending" and order != "Descending":
		os.system('clear')
		print(welcome)
		print('Please select one of the options')
		order = input(
		 "\nWould you like this list to be in [Descending] or [Ascending] order? \n>"
		).title()
	return order


#Sort Selection InputHelper
def directory_input_Helper() -> str:
	commands = ["First Name", "Last Name", "Age"]
	user = input(
	 "\nWould you like to search by [First Name], [Last Name], or [Age]?\n>"
	).title()
	while user not in commands:
		os.system('clear')
		print(welcome)
		print("Please select one of the options")
		user = input(
		 "\nWould you like to sort by [First Name], [Last Name], or [Age]? \n>"
		).title()
	return user


#Leaving Current Screen InputHelper
def leavescreen(directory: Directory) -> None:
	directory.user = input('\nPress [enter] to return to main screen.')
	while directory.user != '':
		print('Please presse [enter] to return to main screen.')
		directory.user = input('\nPress [enter] to return to main screen.')
	directory.screen = 'main'
	os.system('clear')
	print(welcome)


# --------------- MAIN FUNCTION ------------------- #

welcome = colored("           Base Camp Coding Academy Graduate Institute\n",
                  'cyan')


def main() -> None:
	# Variables for Print Statements
	prompt = "Who would you like to search for today?\nTo view our directory, please select [directory]\n> "
	error = "Please put a member's [first name], [last name], [directory], or [quit]\n"
	goodbye = colored('Thank you for showing interest in our cohort!', 'cyan')
	stalk = colored('PREPARE TO BE STALKED', 'red')

	# Rest of Main -----------
	directory = Directory('main', '')
	print(welcome)
	directory.user = input(prompt)
	print("")
	while directory.user.lower() != "quit":
		if inputhelper(directory, cohort_fnames) or inputhelper(
		  directory, cohort_lnames) or inputhelper(directory, cohort_fullnames):
			if directory.user.lower() == 'directory':
				print(stalk)
				directory_selection(directory)
				leavescreen(directory)
			elif directory.user.title() in cohort_fnames or directory.user.title(
			) in cohort_lnames or directory.user.title() in cohort_fullnames:
				search(directory)
				leavescreen(directory)
		else:
			os.system('clear')
			print(welcome)
			print(error)
		directory.user = input(prompt)
		print("")
	print(goodbye)


if __name__ == "__main__":
	main()
