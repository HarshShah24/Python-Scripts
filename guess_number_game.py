import random
print('Hello, What is your Name ?')
name = raw_input()
print('well, ' + name + 'I am thinking of playing a number between 1 and 10')
print('Take a guess')
guess = int(input())
numberToBeGuessed = random.randint(1,10)

for countOfGuess in range(1,7):
  global guess
  if guess > numberToBeGuessed :
        print('Your guess is too high')
        print('Take a guess')
        guess = int(input())
  if guess < numberToBeGuessed :
        print('Your guess is too low')
        print('Take a guess')
        guess = int(input())
  else:
        break;

if numberToBeGuessed == guess:
        print('You guessed it right')
else:
        print ('Better luck next time')

print('You took  number of guess' + str(countOfGuess))
