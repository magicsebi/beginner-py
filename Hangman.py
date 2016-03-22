"""
Hangman game for Python.
This game will run in the terminal.
We will have several functions:
(1) - First function will get the word for the game.
(2) - One function will print the gallows, corresponding to the amount of guesses that have been made.
(3) - One function will print the word along with the blank letters AND will check if the word has been guessed
(4) - The game function. This will be the actual game which will call the previous functions.
The game will also have several difficulty levels. 
"""

#from random import randint
import urllib.request

def getword():
	#This will get expanded so the word can be imported from the web
	#wordlist = ["piece", "average", "brave", "subway", "abstract", "discussion", "crimson", "massive", "hobby", "freaky", "crab", "animatronic", "bughouse", "hothead" "search", "alternate", "emotion", "horoscope"]
	#randomNo = randint(0, len(wordlist)-1)
	#return wordlist[randomNo]
	#End of the old word get.
	url = 'http://randomword.setgetgo.com/get.php'
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	html = response.read().decode('utf-8')
	html = html.lower()
	return html
	
def gallows(strks):
	#This function will print the gallows, depending on how many strikes the user has
	print("\n _______")
	print("|       |")
	if strks == 0:
		print("|\n" * 4)
	elif strks == 1:
		print ("|       O")
		print ("|\n" * 3)
	elif strks == 2:
		print("|       O")
		print("|       |")
		print("|\n" * 2)
	elif strks == 3:
		print("|       O")
		print("|      /|")
		print("|\n" * 2)
	elif strks == 4:
		print("|       O")
		print("|      /|\\")
		print("|\n" * 2)
	elif strks == 5:
		print("|       O")
		print("|      /|\\")
		print ("|      / ")
		print ("|\n")
	elif strks == 6:
		print("|       O")
		print("|      /|\\")
		print("|      / \\")
		print("|\n")
	else:
		pass

		
		
def blankword(word, letterlist):
	"""
	This function will print the word and check if it has been guessed.
	If the word has not been guessed yet, the word will be printed, along with the blanks, and the function will return FALSE
	if the word HAS been guessed, there won't be any blanks printed so the function will return TRUE
	"""
	guesscheck = True
	wordlist = list(word)
	for letter in wordlist:
		if letter in letterlist:
			print(letter + " ", end="")
		else:
			guesscheck = False,
			print("_ ", end="")
	
	return guesscheck

def hangman():
    
	#Get a word, make sure it is a string, create a list with the letters of the word.
	word = getword()
	word = str(word) 
	wordlist = list(word)
	
	#Create an empty set that contains the letters that will be guessed later.
	letterset = []
	
	#Choose a difficulty level.
	print("Choose a level of difficulty:")
	print("(1) Easy: 2 free letters.\n(2) Medium: 1 free letter.\n(3) Hard: No free letters.")
	
	difficulty = input("> ")
	xyz = True 
	while xyz == True: #Next up the free letters are added to the set, depending on the difficulty.
		if difficulty == '3': #No letters for Hard mode.
			xyz = False 
		elif difficulty == '2': #ONE letter for Medium mode. 
			letterset.append(word[0])
			xyz = False
		elif difficulty == '1': #Two letters for Easy mode + check if first and last letter are the same.
			letterset.append(word[0])
			if word[0] != word[-1]:
				letterset.append(word[-1])
				xyz = False
			else:
				xyz = False
		else: #In any other case, the input was garbage. We let the user try again.
			print("Invalid choice. Do you want to try again?\n Enter Y for Yes, any other key for No.")
			difficulty = input("> ")
			difficulty = difficulty.lower()
			if difficulty != "y":
				exit()
			else:
				print("(1) Easy: 2 free letters.\n(2) Medium: 1 free letter.\n(3) Hard: No free letters.")
				difficulty = input("> ")
				difficulty = difficulty.lower()
	
	checkloop = False #Initialize the check if the word has been guessed
	strikes = 0 #Initialize the count for the number of strikes
	blankword(word, letterset) #Print the blank word.
	
	while checkloop == False: #If the word has not been guessed, go through the process!
		gallows(strikes) #Print the gallows, then print the known letters
		print("Letters picked so far:\n", end="")
		for item in letterset:
			print(" %s " % item,  end="")
		
		userloop = True
		while userloop == True: 
			print("\nPick another letter:") #Input a new letter
			letter = input("> ")
			letter = letter.lower()
			if len(letter) >= 2 or letter.isdigit(): #If the input is garbage, choose again
				print("Invalid choice. Choose ONE letter.")
			elif letter in letterset: #if the input has been chosen before, choose again
				print("This letter has been chosen before.")
			else: #If it's a letter and it's new, it's added to the list
				letterset.append(letter)
				userloop = False
		if letter not in wordlist: #if the letter is not in the word, that's a strike
			strikes += 1
		wordcheck = blankword(word, letterset)
		if strikes == 6: #At 6 strikes the game is over.
			print("\nGame over. You are dead.")
			print("The word was: " + word)
			gallows(6)
			exit()
			
		if wordcheck == True:
			print ("Congratulations, you have guessed the word!")
			exit()
			checkloop == True
			

print("Welcome to Hangman for the Terminal.")
hangman()     