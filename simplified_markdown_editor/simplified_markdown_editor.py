
program = True
nothing = False
text = ""

def help():
    print("Available formatters: plain, bold, italic, header, link, inline-code, ordered-list, unordered-list, "
          "new-line \nSpecial commands: !help !done ")


def done():
    global program
    program = False


def user_input():
    user_text = input("Enter your text :>")
    return user_text


while program:
    nothing = False
    key = input("\r" + "Choose a formatter: >")
    match key:
        case "!help":
            help()
            nothing = True
        case "!done":
            with open('output.md', 'w') as f:
                f.write(text)
            done()
            nothing = True
        case "plain":
            text += user_input() + "\n"
            nothing = True
        case "bold":
            text += ("**" + user_input() + "**") + "\n"
            nothing = True
        case "itallic":
            text += ("*" + user_input() + "*") + "\n"
            nothing = True
        case "header":
            level = int(input("Level: > "))
            if level <= 0 or level > 6:
                print("The level should be within the range of 1 to 6. ")
            else:
                text += ("#"*level) + user_input() + "\n"
            nothing = True
        case "link":
            label = "[" + input("Label: ") + "]"
            url = "(" + input("URL: ") + ")"
            text += label + url + "\n"
            nothing = True
        case "inline-code":
            text += ("`" + user_input() + "`" + '\n')
            nothing = True
        case "ordered-list":
            rows = int(input("choose number of rows: > "))
            if rows < 1:
                print("The number of rows should be greater than zero. ")
            else:
                k = 1
                while k <= rows:
                    text += str(k) + ". " + input(f"Row {k}: ") + "\n"
                    k += 1
            nothing = True
        case "unordered-list":
            rows = int(input("choose number of rows: > "))
            if rows < 1:
                print("The number of rows should be greater than zero.")
            else:
                k = 1
                while k <= rows:
                    text += " * " + input(f"Row {k}: ") + "\n"
                    k += 1
            nothing = True
        case "new-line":
            text += '\n'
            nothing = True
    if not nothing:
        print("Unknown formatting type or command! ")
    else:
        print(text.rstrip())

####