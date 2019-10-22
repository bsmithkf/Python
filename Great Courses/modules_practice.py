import random
number=random.randint(1,100)
print(number)

guesses = 1

choice = int(input('What is your number guess? '))
while choice != number:
    if choice > number:
        text = 'Guess lower'
    elif choice < number:
        text = 'Guess higher'
    else:
        text = 'Guess an integer'
    print(text)
    guesses += 1
    choice = int(input('What is your number guess? '))
print('You are right!! It took you',guesses,'guesses!')
