import random

print('Hello, what is your name?')
name = input()

secretNumber = random.randint(1, 20)
print(f'Hello {name}. I am thinking of a number between 1 and 20. Guess the number.')
print(f'Secret number (DEBUG): {secretNumber}') 
found = False

for attempt in range(1, 7):
    print('Take a guess')
    
    guess = int(input())
    if guess == secretNumber:
        print(f"Great! You guessed it correctly in {attempt} attempts") 
        found = True
        break;
    elif guess < secretNumber:
        print('Nope. Your guess is too low')
    else:
        print('Nope. Your guess is too high')

if (not found):   
    print(f"Sorry. You've run out of attempts. The secret number is {secretNumber}")
    