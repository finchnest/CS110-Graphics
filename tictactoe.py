import random

values_dictionary = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}


def check_for_win(mover, sign):
    if (values_dictionary[1] == values_dictionary[2] == values_dictionary[3] == sign) or (
            values_dictionary[4] == values_dictionary[5] == values_dictionary[6] == sign) or (
            values_dictionary[7] == values_dictionary[8] == values_dictionary[9] == sign) or (
            values_dictionary[1] == values_dictionary[4] == values_dictionary[7] == sign) or (
            values_dictionary[2] == values_dictionary[5] == values_dictionary[8] == sign) or (
            values_dictionary[3] == values_dictionary[6] == values_dictionary[9] == sign) or (
            values_dictionary[7] == values_dictionary[5] == values_dictionary[3] == sign) or (
            values_dictionary[1] == values_dictionary[9] == values_dictionary[5] == sign):
        print(mover + " won")
        return [True, "win"]
    else:
        arr = [9]
        for k, v in values_dictionary.items():
            arr.append(bool(v))
        if all(arr):
            print("tie")
            return [False, "tie"]
        return [False, ""]


def value_precense_checker():
    return


def printUpdatedBoard():
    print(values_dictionary[7] + "      |" + values_dictionary[8] + "       |" + values_dictionary[9])
    print("-" * 15)
    print(values_dictionary[4] + "      |" + values_dictionary[5] + "       |" + values_dictionary[6])
    print("-" * 15)
    print(values_dictionary[1] + "      |" + values_dictionary[2] + "       |" + values_dictionary[3])


def computerMove(mark):
    empty_vals = []
    for k in values_dictionary:
        if (values_dictionary[k] != "x") and (values_dictionary[k] != "o"):
            empty_vals.append(k)
    if (len(empty_vals) > 0):
        chosen = random.choice(empty_vals)
        values_dictionary[chosen] = mark
        print("computer selected ", chosen)


def user_move(mark):
    try:
        move = int(input("Where do you want to go (1-9)? "))
        if bool(values_dictionary[move]) == True:
            print("make another move, the space is occupied: ")
            user_move(mark)
        else:
            values_dictionary[move] = mark
            print("You have selected ", move)

    except:
        print("make a right move please ")
        user_move(mark)


user_choice = input("Do you want to be x or o? ")
comp_choice = ""

if (user_choice == "x"):
    comp_choice = "o"
elif (user_choice == "o"):
    comp_choice = "x"
go_first = input("Do you " + str(user_choice).capitalize() + " wanna go first? (y/n) ")
starter = ""
if (go_first == "y"):
    starter = "user"
else:
    starter = "comp"
ctr = 7
while ctr > 0:
    for x in range(ctr, ctr + 3):
        print(str(x) + "  | ", end=" ")
    ctr -= 3
    print("\n")
    if (ctr != -2):
        print("-" * 15)
while True:

    if (starter == "user"):
        user_move(user_choice)
        printUpdatedBoard()
        check_for_win("user", user_choice)
        if (check_for_win("user", user_choice)[0]):
            break
        elif (check_for_win("user", user_choice)[1] == "tie"):
            break
        computerMove(comp_choice)
        printUpdatedBoard()
        check_for_win("comp", comp_choice)
        if (check_for_win("comp", comp_choice)[0]):
            break
        elif (check_for_win("comp", comp_choice)[1] == "tie"):
            break
    else:
        computerMove(comp_choice)
        printUpdatedBoard()
        check_for_win("comp", comp_choice)
        if (check_for_win("comp", comp_choice)[0]):
            break
        elif (check_for_win("comp", comp_choice)[1] == "tie"):
            break
        user_move(user_choice)
        printUpdatedBoard()
        check_for_win("user", user_choice)
        if (check_for_win("user", user_choice)[0]):
            break
        elif (check_for_win("user", user_choice)[1] == "tie"):
            break
