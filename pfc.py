import random
running = True
list1 = ["pebble", "paper", "scissor"]

while running:


    result_ia = random.choice(list1)
    result = input("Pebble, paper, scissors, ...")

    if result_ia == "pebble" and result == str("scissor"):

        print("You loose!")
        running = False

    elif result_ia == "pebble" and result == str("paper"):

        print("You win!")
        running = False

    elif result_ia == "paper" and result == str("scissor"):

        print("You win!")
        running = False

    elif result_ia == "scissor" and result == str("paper"):

        print("You loose!")
        running = False

    elif result_ia == "scissor" and result == str("pebble"):

        print("You win!")
        running = False

    elif result_ia == "paper" and result == str("pebble"):

        print("You loose!")
        running = False

    else:

        print("Retry putasss!")

        continue

