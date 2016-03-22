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

from random import randint
import urllib2

def getword():
	#This will get expanded so the word can be imported from the web
	#wordlist = ["piece", "average", "brave", "subway", "abstract", "discussion", "crimson", "massive", "hobby", "freaky", "crab", "animatronic", "bughouse", "hothead" "search", "alternate", "emotion", "horoscope"]
	#randomNo = randint(0, len(wordlist)-1)
	#return wordlist[randomNo]
	#End of the old word get.
	response = urllib2.urlopen('http://randomword.setgetgo.com/get.php')
	html = response.read()
	return html
	
def gallows(strks):
	#This function will print the gallows, depending on how many strikes the user has
	if strks >= 7 or strks < 0:
		exit()
	print "\n _______"
	print "|       |"
	if strks == 0:
		print "|\n" * 4
	elif strks == 1:
		print "|       O"
		print "|\n" * 3
	elif strks == 2:
		print "|       O"
		print "|       |"
		print "|\n" * 2
	elif strks == 3:
		print "|       O"
		print "|      /|"
		print "|\n" * 2
	elif strks == 4:
		print "|       O"
		print "|      /|\\"
		print "|\n" * 2
	elif strks == 5:
		print "|       O"
		print"|      /|\\"
		print "|      / "
		print "|\n"
	elif strks == 6:
		print "|       O"
		print "|      /|\\"
		print "|      / \\"
		print "|\n"
		print "\nGame over."
		exit()
	else:
		pass


		
def blankword(word, letterlist):
	fullcheck = True
	"""
	This function will check if the word has been guessed.
	If the word has not been guessed yet, the word will be printed along with the blanks.
	if the word HAS been guessed, the word will be printed and a True check will be returned
	"""
	for letter in word:
		if letter in letterlist:
			print letter + " ",
		else:
			fullcheck = False
			print "_ ",
		
	if fullcheck == True:
			print "Congratulations! You have guessed the word."
			exit()
	return fullcheck

def hangman():
    
	word = getword()
	word = str(word)
	print word
	#Now we have the word.
	print "Choose a level of difficulty:"
	print "(1) Easy: 2 free letters.\n(2) Medium: 1 free letter.\n(3) Hard: No free letters."
	difficulty = raw_input("> ")
	#Now we have the difficulty.
	
	letterset = []
	#Now we have an empty set that contains the guessed letters.
	xyz = True
	#Next up the free letters are added to the set.
	while xyz == True:
		if difficulty == '3':
			xyz = False
		elif difficulty == '2':
			letterset.append(word[0])
			xyz = False
		elif difficulty == '1':
			letterset.append(word[0])
			if word[0] == word[-1]:
                #If the first letter is the same as the last letter, there's no need to add it again.
                #This way we also avoid any errors.
				pass
			else:
				letterset.append(word[-1])
				#Add the last letter to the set too.
				xyz = False
		else:
			print "Invalid choice. Do you want to try again?\n Enter Y for Yes, any other key for No."
			choice = lower(raw_input("> "))
			if choice != "y":
				exit()
			else:
				print "(1) Easy: 2 free letters.\n(2) Medium: 1 free letter.\n(3) Hard: No free letters."
				difficulty = int(raw_input("> "))
	wordcheck = False
	#This checks if the word has been guessed
	strikes = 0
	#this variable counts the number of strikes
	blankword(word, letterset)
	while wordcheck == False:
		#If the word has not been guessed, we go through the process!
		gallows(strikes)
		#Print the gallows, then print the known letters
		if len(letterset) >= 1:
			print "Letters picked so far:"
			for item in letterset:
				print " %s " % item,
		else:
			pass
		
		#Now we get user input
		userloop = True
		while userloop == True:
			print "Pick another letter:"
			userchoice = raw_input("> ")
			userchoice.upper
			if len(userchoice) >= 2:
				print "Invalid choice. Choose only one letter."
			elif userchoice in letterset:
				print "The letter has been chosen before."
			else:
				letterset.append(userchoice)
				userloop = False
        #Now we check if the letter is in the word
		wordlist = list(word)
		wordcheck = blankword(word, letterset)
		if userchoice not in wordlist:
			strikes += 1
            
    
print "Welcome to Hangman for the Terminal."
hangman()
        
        