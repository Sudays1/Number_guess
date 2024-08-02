import random
def start():
    x = random.randint(1, 10)
    while True:
        guess = int(input("Enter a number between 1 and 10: "))
        if guess == x:
            print("Correct!")
            break
        else:
            print("Incorrect!")
start()