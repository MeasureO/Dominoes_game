import random
pieces = []
for i in range(0, 7):
    for j in range(0, 7):
        if i <= j:
            pieces.append([i, j])

#print(len(pieces))
random.shuffle(pieces)
stock = pieces[:14]
computer =  pieces[14:21]
player = pieces[21:28]
maximum = 0
max_piece = [0, 0]
for i in range(0, 7):
    for j in range(0, 7):
        if i == j and [i, i] in pieces[14:28] and i > maximum:
            max_piece = [i, i]
            
if max_piece in computer:
    computer.remove(max_piece)
    status = "player"
else:
    player.remove(max_piece)
    status = "computer"

        
    
    
board = [max_piece]
while True:
    print("=" * 70)
    print("Stock size:", len(stock))
    print("Computer pieces:", len(computer))
    print()
    if len(board) <= 6:
        print(*board, sep='')
    else:
        print(*board[:3], sep='', end='')
        print('...', end='')
        print(*board[-3:], sep='')
    print()
    for i, elem in enumerate(player):
        print(i + 1,':', elem, sep='')
    print()
    if status == "The game is over. It's a draw!":
        print("Status:", "The game is over. It's a draw!")
        break
    elif status == "The game is over. You won!":
        print("Status:", "The game is over. You won!")
        break 
    elif status == "The game is over. The computer won!":
        print("Status:", "The game is over. The computer won!")
        break
    elif status == "player":
        print("Status:",  "It's your turn to make a move. Enter your command.")
    elif status == "computer":
        print("Status:", "Computer is about to make a move. Press Enter to continue...")
    while True:
        command = input()
        if status == "player" and int(float(command)) == int(command) and -len(player) <= int(command) <= len(player):
            while True:
                command = int(command)
                if command == 0:
                    choice = random.choice(stock)
                    player.append(choice)
                    stock.remove(choice)
                    status = "computer"
                    break
                elif command > 0:
                    #if set(player[command - 1]) & set(board[-1]) == set():
                    if board[-1][1] not in player[command - 1]:
                        print("Illegal move. Please try again.")
                        break
                    else:
                        if board[-1][1] == player[command - 1][0]:
                            board.append(player[command - 1])
                        else:
                            player[command - 1].reverse()
                            board.append(player[command - 1])
                            
                        del player[command - 1] 
                    status = "computer"
                    break 
                elif command < 0:
                    command = abs(command)
                    if board[0][0] not in player[command - 1]:
                        print("Illegal move. Please try again.")
                        break
                    else:
                        if board[0][0] == player[command - 1][1]:
                            board.insert(0, player[command - 1])
                        else:
                            player[command - 1].reverse()
                            board.insert(0, player[command - 1])
                        del player[command - 1]
                    status = "computer"
                    break
                # choice = random.choice(stock)
                # player.append(choice)
                # stock.remove(choice)
                # status = "computer"
                # break
            break
                
        elif status == "computer":
            minus_move = '-'
            plus_move = '+'
            #zero_move = '0'
            #move = [minus_move, plus_move, zero_move]
            move = [minus_move, plus_move]
            
            command = random.choice(move)
            dictionary = {}
            for i in range(10):
                dictionary[i] = 0
            for elem in (board + computer):
                for num in elem:
                    dictionary[num] += 1
            #print(computer)
            rate = {}
            for elem in computer:
                rate[tuple(sorted(elem))] = dictionary[elem[0]] + dictionary[elem[1]]
            #print(rate)
            rate = sorted(rate.items(), key=lambda x: x[1], reverse=True)
            #print(rate)
            #max_choice = max(rate, key=lambda x: x[1])
            #print(max_choice)
            while True:
                if len(rate) > 0:
                    #choice = random.choice(computer)
                    choice = max(rate, key=lambda x: x[1])
                    print(choice)
                    if board[-1][1] in choice[0] or board[0][0] in choice[0]:
                        if board[-1][1] == choice[0][0]:
                            board.append(list(choice[0]))
                        elif board[-1][1] == choice[0][1]:
                            nchoice = list(choice[0])
                            nchoice.reverse()
                            board.append(nchoice)
                        elif board[0][1] == choice[0][1]:
                            board.insert(0, list(choice[0]))
                        elif board[0][1] == choice[0][1]:
                            nchoice = list(choice[0])
                            nchoice.reverse()
                            board.insert(0, nchoice)
                        computer.remove(list(choice[0]))
                        status = "player"
                        break
                    else:
                        rate.remove(choice)
                       #print(rate)
                        continue
                else:
                    r_choice = random.choice(stock)
                    #choice = max_choice
                    computer.append(r_choice)
                    stock.remove(r_choice)
                    status = "player"
                    break
                
                    
                
        else:
            print("Invalid input. Please try again.")
            continue
        break
        
    
        
    if len(stock) == 0:
        status = "The game is over. It's a draw!"
    if len(player) == 0:
        status = "The game is over. You won!"
    if len(computer) == 0:
        status = "The game is over. The computer won!"
        

        
        
        
        
        
