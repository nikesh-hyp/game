import random
ch_1 = ch_2 = ch_3 = ch_4 = -1
game_over = False


def turn():
    print("Type \"r\" to roll")
    des = input(":")
    if des == "r":
        rand = random.randrange(1, 7)
        print("You rolled : ",rand,"\n")
        return rand


def green():
    print('\033[92m Green\'s Turn!''\033[0m')
    returned_g = turn()
    pos_g = ch_1

    if pos_g < 0:
        if returned_g == 1:
            pos_g = 0
            returned_g = turn()
            pos_g = pos_g + returned_g
            print("You are at: ", pos_g, "\n")
            return pos_g
        else:
            return -1
    else:
        pos_g = pos_g + returned_g
        print("You are at: ", pos_g, "\n")
        return pos_g


def red():
    print('\033[31m Red\'s Turn!''\033[0m')
    pos_r = ch_2
    returned_r = turn()

    if pos_r < 0:
        if returned_r == 1:
            pos_r = 0
            returned_r = turn()
            pos_r = pos_r + returned_r
            print("You are at: ", pos_r, "\n")
            return pos_r
        else:
            return -1
    else:
        pos_r = pos_r + returned_r
        print("You are at: ", pos_r, "\n")
        return pos_r


def blue():
    print('\033[34m Blue\'s Turn!''\033[0m')
    pos_b = ch_3
    returned_b = turn()

    if pos_b < 0:
        if returned_b == 1:
            pos_b = 0
            returned_b = turn()
            pos_b = pos_b + returned_b
            print("You are at: ", pos_b, "\n")
            return pos_b
        else:
            return -1
    else:
        pos_b = pos_b + returned_b
        print("You are at: ", pos_b, "\n")
        return pos_b


def yellow():
    print('\033[33m Yellow\'s Turn!''\033[0m')
    pos_y = ch_4
    returned_y = turn()

    if pos_y < 0 :
        if returned_y == 1:
            pos_y = 0
            returned_y = turn()
            pos_y = pos_y + returned_y
            print("You are at: ", pos_y, "\n")
            return pos_y
        else:
            return -1
    else:
        pos_y = pos_y + returned_y
        print("You are at: ", pos_y, "\n")
        return pos_y


while not game_over:
    ch_1 = green()
    if ch_1 >= 30:
        game_over = True
        print('\033[32m Green Won!!''\033[0m')
        break
    ch_2 = red()
    if ch_2 >= 30:
        game_over = True
        print('\033[31m Red Won!''\033[0m')
        break
    ch_3 = blue()
    if ch_3 >= 30:
        game_over = True
        print('\033[34m Blue Won!''\033[0m')
        break
    ch_4 = yellow()
    if ch_4 >= 30:
        game_over = True
        print('\033[33m Yellow Won!''\033[0m')
        break


if game_over:
    print('\033[92m GAME OVER''\033[0m')