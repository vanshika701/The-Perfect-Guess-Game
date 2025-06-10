import random
print("Game has started!")
number = random.randint(5, 50)
guessNumber=int(input("Enter your guess: "))
guesses=1
while(number !=guessNumber):
    guesses+=1
    if(guessNumber<number):
        print("Your guess is very small")
        guessNumber=int(input("Enter a higher number: "))
    elif(guessNumber>number):
        print("Your guess is very high")
        guessNumber=int(input("Enter a lower number: "))
        
print("Congratulations! You guessed the number correctly.")
print(f"You guessed the number in {guesses} attempts.")




