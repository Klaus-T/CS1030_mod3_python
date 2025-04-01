import random
#this import the random
number = random.randint(0,100)
#this sets that the "number" will now generate a random integer from 0-100
print("Guess the magic number between 0 and 100")
#this just displays the words
guess = -1 
while guess !=number:
    #this is for the number the user inputs
    guess = int(input("\nEnter your guess:"))
    if guess == number:
        print(f"Yes, the number is {number}")
        #if the guess integer is equal to the number it will print that text
    elif guess > number:
        print("Your guess is too high")
        #if the guess integer is greater than the number, it will print the dialoge above
    else:
        print("Your guess is too low")
        #this is the else for if the integer is less than the number, then it prints the dialoge
    