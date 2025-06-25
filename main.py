import random, sys, time, colorama
from colorama import Fore
# code for keeping track of guesses
guesses = 0

# type writer function
def typewriter(message):
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()

    if char != '\n':
      time.sleep(0.05)
    else:
      time.sleep(0.5)

# Tutorial
initiate_tutorial = input('Would you like a tutorial? yes(y) or no(type anything) ')
if initiate_tutorial.lower() == 'y':
  start_message = 'Welcome to this number guessing game! \n\
  You will have to guess a number in as few guesses as posibble \n\
  You will first be asked to insert the max number to guess,\n\
  enter a smaller number for an easier game or a larger one for a longer game.\n\
  Goodluck!'

  typewriter(start_message)
  print('####################################')

  # code for getting max of range & making sure its a number
  top_of_range = input('Type the maximum number: ')

else:
# code for getting max of range & making sure its a number
    top_of_range = input('Type the maximum number: ')

if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:
    print('Please type a number larger than 0 next time')
    quit()

else:
  print('Please type a number next time')

# code for generating number and getting users guess
num = random.randint(0, top_of_range)
  
# code for repeating the users guess until he answers right & updating guesses
while True:
  guesses += 1
  print('\033[39m') #changes the colour back to default
  user_num = input('Guess the number: ')
  if user_num.isdigit():
    user_num = int(user_num)
  else:
    print('Please type a number next time')
    continue
# code for checking if guess was correct and printing the amount of guesses it took
  if user_num == num:
    print(f"{colorama.Fore.GREEN}Correct! You guessed the number in {guesses} guess(es)!")
    break
    
  else:
    print(f"{Fore.RED}You got it wrong!")