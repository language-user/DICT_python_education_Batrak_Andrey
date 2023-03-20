import random


class Test:
    def __init__(self, r_n1, r_n2, operation_random, user_answer):
        self.r_n1 = r_n1
        self.r_n2 = r_n2
        self.operation_random = operation_random
        self.user_answer = int(user_answer)

    def operation(self):
        char = self.operation_random
        result = 0
        match char:
            case '+':
                result = self.r_n1 + self.r_n2
            case '-':
                result = self.r_n1 - self.r_n2
            case '*':
                result = self.r_n1 * self.r_n2
            case 'sqrt':
                result = self.r_n1 * self.r_n1
        return result

    def right_check(self):
        right_answer = self.operation()
        if self.user_answer == right_answer:
            return "Right!"
        else:
            return "Wrong!"


def arithmetic_test(test_level):
    i = 0
    mark = 0
    while i < 5:
        if test_level == "1":
            test = Test(random.randint(2, 9), random.randint(2, 9), random.choice(['+', '-', '*']), 0)
            print(test.r_n1, test.operation_random, test.r_n2)
            test.user_answer = input(">")
        else:
            test = Test(random.randint(11, 29), 0, 'sqrt', 0)
            print(test.r_n1)
            test.user_answer = input(">")
        while not test.user_answer.lstrip("-").isdigit():
            print("Incorrect format!")
            test.user_answer = input(">")
        test.user_answer = int(test.user_answer)
        print(test.right_check())
        if test.right_check() == "Right!":
            mark += 1
        i += 1
    print(f"Your mark is {mark}/5")
    save_to_file = input("Would you like to save your result to the file? \nEnter yes or no.\n")
    if "Y" in save_to_file or 'y' in save_to_file:
        name = input("Enter your name:")
        with open("results.txt", "w") as file:
            if test_level == '1':
                file.write(f"{name}: {mark}/5 in level {level}: simple operations with numbers 2-9")
            else:
                file.write(f"{name}: {mark}/5 in level {level}: integral squares of 11-29")


level = input('''
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29 \n''')


while level != "1" and level != "2 ":
    print("Incorrect format!!!")
    level = input('''
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29 \n''')

arithmetic_test(level)