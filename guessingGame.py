import random
guess=random.randint(1,9)
chances=5

while < 5:
    gues=int(input("Guess a number between 1 and 9"))
    if gues < guess:
        print("The number which you have guessed is smaller than the random number.")
        chances=chances-1  
    elif gues > guess:
         print("The number is smaller than the number thaat you have guessed.")
         chances=chances-1
    else:
        print("Invalid input")

    if gues==guess:
        print("You have guessed correctly. Well Done!")    
        break

    if chances=0:
        print("You have run out of chances")

    

   


    




