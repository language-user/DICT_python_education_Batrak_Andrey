import random

domino = [[x,y]for x in range(7) for y in range(x,7)]
players = []
while len(players) != 14:
    dom = random.choice(domino)
    players.append(dom)
    domino.remove(dom)
player, computer = players[:7],players[7:]
m = [i for i in players if i[0] == i[1]]
max_n = -1
n = []
for i in m:
    if i[0] > max_n:
        max_n = i[0]
        n = i
if n in player:
    player.remove(n)
    status = "computer"
else:
    computer.remove(n)
    status = "player"


def play_f():
    print("="*70)
    print("Stock size:{}".format(len(domino)))
    print("Computer pieces:{}".format(len(computer)))
    if len(pov)>6:
        print("\n{}{}{}...{}{}{}\n".format(*pov[:3],*pov[-3:]))
    else:
        print("\n{}\n".format(pov))
    for i in range(len(player)):
        print("{}:{}".format(i + 1, player[i]))


def computer_t():
    klv1 = [*pov,*computer]
    q = []
    dom1 = 0
    for i in range(7):
        for a in klv1:
            for d in range(len(a)):
                if  i == a[d]:
                    dom1 += 1
        q.append(dom1)
        dom1 -= dom1
    q_1 = {i:q[i] for i in range(len(q))}
    slov = []
    br = []
    for i in computer:
        if pov[0][0] in i or pov[-1][1] in i:
            br.append(i)
    if len(br) == 0:
        computer.append(domino[0])
        domino.remove(domino[0])
    else:
        for i in range(len(br)):
            for j in range(len(br[i])):
                dom1 += q_1[br[i][j]]
            slov.append(dom1)
        z = {slov[i]: i for i in range(len(br))}
        p = br[z[slov[0]]]
        if p[1] == pov[0][0]:
            pov.insert(0, p)
        elif p[0] == pov[0][0]:
            pov.insert(0, p[::-1])
        elif p[0] == pov[-1][1]:
            pov.append(p)
        elif p[1] == pov[-1][1]:
            pov.append(p[::-1])
        computer.remove(p)


pov = [n]
play_f()
while True:
    if status == "computer":
        print(input("Status:Computer is about to make a move.Press Enter to continue...\n" ))
        computer_t()
        status = "player"
    else:
        print("Status:It's your turn to make a move. Enter your command." )
        while True:
            image = input()
            try:
                int(image)
            except ValueError:
                print("Invalid input. Please try again." )
                continue
            else:
                if int(image) in range(-len(player), len(player)+1):
                    dom1 = int(image)
                    if dom1 > 0:
                        if player[dom1-1][0] == pov[-1][1]:
                            pov.append(player[dom1-1])
                            player.remove(player[dom1-1])
                        elif player[dom1-1][1] == pov[-1][1]:
                            pov.append(player[dom1-1][::-1])
                            player.remove(player[dom1-1])
                        else:
                            print("Illegal move. Please try again." )
                            continue
                        break
                    elif dom1 < 0:
                        if player[-dom1-1][1] == pov[0][0]:
                            pov.insert(0, player[-dom1-1])
                            player.remove(player[-dom1-1])
                        elif player[-dom1-1][0] == pov[0][0]:
                            pov.insert(0, player[-dom1-1][::-1])
                            player.remove(player[-dom1-1])
                        else:
                            print("Illegal move. Please try again.")
                            continue
                        break
                    else:
                        player.append(domino[0])
                        domino.remove(domino[0])
                        break
                else:
                    print("Invalid input. Please try again.")
                    continue
        status = "computer"
    play_f()
    if len(computer) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif len(player) == 0:
        print("Status: The game is over. You won!")
        break
    elif pov[0][0] == pov[-1][-1]:
        c = 0
        for x in range(len(pov)):
            for h in pov[x]:
                if h == pov[0][0]:
                    c += 1
        if c == 8:
            print("Status: The game is over. It's a draw!")
            break