import random
print("Welcome to the UPPER / LOWER game\n")
print("You should guss what the next number will be\n")
print("Get started...\n")
while True:
    count = 0
    number_1 = random.randint(1, 9)
    number_2 = random.randint(1, 9)
    txt = "GAME OVER!"
    x = txt.center(30)
    print("My number is", number_1, "next number will be ?\nU for UPPER / L for LOWER:")
    guess: str = input()
    if guess == "U":
        print("Next number is:", number_2)
        if number_1 < number_2:
            print("NICE :), CORRECT\n")
            count += 1
        elif number_1 == number_2:
            print("NICE :), CORRECT\n")
            count += 1
        else:
            print("Ohh, you lost :(")
            print("Your final score is:",count)
            print(x)
            break
    if guess == "L":
        print("Next number is:", number_2)
        if number_1 > number_2:
            print("NICE :), CORRECT\n")
            count += 1
        elif number_1 == number_2:
            print("NICE :), CORRECT\n")
            count += 1
        else:
            print("Ohh, you lost :(")
            print("Your final score is:",count)
            print(x)
            break
