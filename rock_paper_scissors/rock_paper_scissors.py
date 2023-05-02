import random

items = {"paper": ["rock", "air", "water", "dragon", "devil", "lighting", "gun"],
         "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"],
         "lighting": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
         "devil": ["lighting", "gun", "rock", "fire", "scissors", "snake", "human"],
         "scissors": ["snake", "human", "tree", "wolf", "sponge", "paper", "air"],
         "dragon": ["devil", "lighting", "gun", "rock", "fire", "scissors", "snake"],
         "rock": ["fire", "scissors", "snake", "human", "tree", "wolf", "sponge"],
         "water": ["dragon", "devil", "lighting", "gun", "rock", "fire", "scissors"],
         "air": ["water", "dragon", "devil", "lighting", "gun", "rock", "fire"],
         "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lighting"],
         "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
         "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
         "sponge": ["paper", "air", "water", "dragon", "devil", "lighting", "gun"],
         "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"],
         "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"]}
x = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
name = str(input("enter your name: "))
print(f"Hello: {name}")
el = input("choose the elements: ")
list = el.split(",")


def standard():
    while True:
        point = 0
        r = open('rating.txt', 'r')
        for context in r:
            nick, score = context.split()
            if name == nick:
                point = int(score)
        cmp = random.choice([*x.keys()])
        pl = str(input(""))
        if pl == "rating":
            print(f"your score: {point}")
        if pl == "exit":
            r.close()
            print("Bye")
            break
        if pl == cmp:
            print("Draw")
            point += 50
            continue
        elif pl == x.get(cmp):
            print(f"Sorry, but the computer chose {cmp}")
            continue
        elif x.get(pl) == cmp:
            print(f"Well done. The computer chose {cmp} and failed ")
            point += 100
            continue
        else:
            print("Choose the item! ")
            continue


def extend():
    while True:
        point = 0
        r = open('rating.txt', 'r')
        for context in r:
            nick, score = context.split()
            if name == nick:
                point = int(score)
        cmp = random.choice(list)
        pl = str(input(""))
        if pl == "rating":
            print(f"Your score: {point}")
        elif pl == "exit":
            print("Bye!")
            break
        elif pl not in list:
            print("you don't choose that ")
            continue
        elif pl == cmp:
            print("Draw")
            point += 50
        elif pl in items.get(cmp):
            print(f"Sorry, but the computer chose {cmp}")
        elif cmp in items.get(pl):
            print(f"Well done. The computer chose {cmp} and failed ")
            point += 100
        else:
            print("Invalid input")


while True:
    if el == "":
        print("Okay, let's go")
        standard()
    else:
        print("Okay,let's go")
        extend()