print("Hello!  My name is Chatbot1.\nI was created in 2022.")

name = input("Please, remind me your name.\n> ")

print("What a great name you have, {0}".format(name))

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {0}; that's a good time to start programming!".format(age))
num = int(input("Now I will prove to you that I can count to any number you want.\n> "))

i = 0
while i <= num:
    print(i)
    i = i + 1

print("Let's test your programming knowledge.")
print("What laguages are similar to python")

print("1. C++\n2. Pascal\n3. C#\n4. Ruby\n5. Java")
answer = int(input("> "))

while answer != 4:
    print("Please, try again")
    answer = int(input("> "))
    ...
print("Completed, have a nice day!\nCongratulations, have a nice day!")
