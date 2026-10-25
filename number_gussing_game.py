import random
bot_num = random.randint(0,2)
success = False

while True:
    try:
        user_guess = int(input("Guess a number from 0 to 20\n>> "))
        attempts = 1

        while True:
            if bot_num == user_guess:
                print(f"Congrats, you guessed the right number in just {attempts} attempts.")
                success = True
                break
            else:
                if user_guess > 20 or user_guess < 0:
                    print("Invalid input. Make sure your guess is between 0 and 20")
                elif user_guess > bot_num:
                    print("Your guess is higher, try low.")
                elif user_guess < bot_num:
                    print("Your guess is lower, try high.")
                else:
                    print("Invalid")
                attempts += 1
                user_guess = int(input("Make another guess.\n>> "))
    except:
        print("Make sure your guess is a numerical value in decimals between 0 and 20.")
    if success:
        break