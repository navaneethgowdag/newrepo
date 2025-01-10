import random

def game():
    print('Welcome to the game!!')
    print('Guess The Number From 1 to 100. (YOU GOT 5 CHANCES)')
    choice = random.randint(1,100)
    for i in range(6): 
        try:
            num = int(input("Enter a number: "))
            if num > choice:
                print('Number is greater than the secret number')
            elif num < choice:
                print('Number is lesser than the secret number')
            elif num == choice:
                print('You guessed the correct number!')
                print('You won!')
                break
        except ValueError: 
            print("Invalid input. Please enter a valid number.")
            
    else:
        print('You lost your chances, you lost.')
        print(f'secret number is {choice}')

game()
