# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

#!/bin/python


import time
import random
import os

def game():
 attempts = 5
 guesses = ''
 l = len(word)
 q = list(word)
 y = []
 z = [""]
 omit = []
 c1 = "            *"
 c2 = "           *"
 c4 = "Correct * * "
 c3 = "         *  "
 print()
## print("Last letter of the word is" , q[-1:]) ##
 so = sorted(q, key=str.lower)
 while attempts > 0:
  guess = input("guess a letter in a word: ")
  print()
  guesses += guess
  if guess == z[0]:
   attempts -= 1
   print("XXXXXXXXXXXXXXX")
   print("X    Wrong    X ")
   print("XXXXXXXXXXXXXXX")
   print("\n")
   print("You have", +attempts, "more guesses")
   print("---------------------")
  if guess not in word:
   attempts -= 1
   print("XXXXXXXXXXXXXXX")
   print("X    Wrong    X ")
   print("XXXXXXXXXXXXXXX")
   print("\n")
   print("You have", +attempts, "more guesses")
   print("---------------------")
   omit.append(guess)
   print ("Letters in the word are= ",y)
   print("Letters NOT in the word so far= ",omit, "\n" )
  if guess in word:
   print(repr(c1))
   print(repr(c2))
   print(repr(c4))
   print(repr(c3))
   co = q.count(guess)
   li = y.count(guess)
   if word.startswith(guess) == True:
     print("*************   CLUE  ****************")
     print("This is the first letter of the word: ",guess)
   if word.endswith(guess) == True:
     print("*************   CLUE  ****************")
     print("This is the last letter of the word: ",guess)
   if guess in y:
    print(repr(c1))
    print(repr(c2))
    print(repr(c4))
    print(repr(c3))
    if li == co == 1:
     print("*********************************")
     print("* But Letter is already guessed *")
     print("*********************************")
     print("-------------------")
     y.pop()
   if co > 1:
    if li == co:
     print("************************************************************************************")
     print("   You have already inserted letter sufficient times. Hence, reducing one attempt   ")
     print("************************************************************************************")
     print("You have", +attempts, "more guesses")
     print("---------------------")
     y.pop()
     attempts -= 1
    else:
     print("**************************************************************")
     print  ("Letter is occuring for follwing number of times in a word  ")
     print                        (co,"Times")
     print("**************************************************************")
     print("--------------------")
     co -= co
   print("---------------------")
   y.append(guess)
   print ("Letters in the word are= ",y)
   print("Letters NOT in the word so far= ",omit,"\n")
   if len(y) == len(so):
    sorted(y, key=str.lower)
    print("You won",name,".Word is",word)
    input( "\n" )
    break
  if attempts == 0:
   print("Word was",word)
   print("You lost")
   input( "\n" )
 return;


name=input("What is your name? \n")
print("Hello", name ,"time to play hangman!")
print("")
time.sleep(1)

print("*******************************")
print("*     Hangman game starts     *")
print("*                             *")
print("*You have to guess a word in  *")
print("*         5 attempts          *")
print("*******************************")
print("Choose your difficulty")
print("1 (Easy)")
print("2 (Medium)")
print("3 (Hard)")
print("")
x = int(input())
print("")
movie = ["titanic", "dunkirk", "shrek", "godzilla", "frankenstein", "batman", "avengers", "madagascar", "spiderman", "avatar", "inception", "conjuring", "annabelle", "cars", "deadpool", "thor"]
cities = ["washim", "jamkhed", "gondia", "wardha", "ambejogai", "nandurbar", "tarkarli", "sindhudurg", "gadchiroli", "vengurla", "malegaon", "pandharpur", "shirdi", "miraj", "gadhinglaj", "pirangut"]
countries = ["lesotho", "ghana", "eritrea", "liechtenstein", "montenegro", "botswana", "rwanda" , "djibouti", "angola", "azerbaijan", "brunei", "curacao", "guatemala", "kyrgyzstan", "mozambique", "qatar", "luxombourg", "mauritania", "benin", "chad"]


if (x > 3):
 print("Value is out of Range")
if (x == 1):
 word=(random.choice(movie))
 print("A hollywood movie name is decided for guessing")
 print("Letters in the name are",len(word))
 print("You have 5 attempts to guess it\n")
 game()
if (x == 2):
 word=(random.choice(cities))
 print("A Maharshtian city name is decided for guessing")
 print("Letters in the name are",len(word))
 print("You have 5 attempts to guess it\n")
 game()
if (x == 3):
 word=(random.choice(countries))
 print("A country name is decided for guessing")
 print("Letters in the name are",len(word))
 print("You have 5 attempts to guess it\n")
 game()