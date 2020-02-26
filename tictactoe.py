values_dictionary = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

while True:
    user_choice = input("Do you want to be x or o?")
    comp_choice = ""

    if (user_choice == "x"):
        comp_choice = "o"
    elif (user_choice == "o"):
        comp_choice = "x"
    go_first = input("do you wanna go first?")
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
    break

    move = input("make a move: ")
    try:
        if move.isalnum() and (9 > move > 0):
            if values_dictionary[move] != "":
                move = input("make another move, the space is occupied: ")
                printUpdatedBoard()
            else:
                values_dictionary[move] = user_choice



    except:
        move = input("make a right move please : ")
