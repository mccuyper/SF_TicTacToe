# Creating 10 empty values for playfield. from 0 to 9(0 is always gonna be empty)
board = [' ' for x in range(10)]


def printBoard(board):
    """
        Функция выводит игровое поле в консоль. Print the board
    """
    print('1    |2    |3   ')
    print('  ' + board[1] + '  | ' + board[2] + '   | ' + board[3])
    print('     |     |   ')
    print('------------------')
    print('4    |5    |6   ')
    print('  ' + board[4] + '  | ' + board[5] + '   | ' + board[6])
    print('     |     |   ')
    print('------------------')
    print('7    |8    |9   ')
    print('  ' + board[7] + '  | ' + board[8] + '   | ' + board[9])
    print('     |     |   ')


# Функция заполняет позицию с Х или О. Fill the particular position(pos) with the letter('X' or 'O')
def insertLetter(letter, pos):
    board[pos] = letter


# Проверка занято ли место на игровом поле. Return True if position on board is free, and False if occupied
def spaceIsFree(pos):
    return board[pos] == ' '


def isBoardFull(board):
    """
        Функция проверяет остались ли пустые клетки на поле
        Х всегда ходит последним

        Check for empty spaces on the board
        func count() go through a board list and count
        amount of " " empty strings
        count can be equil 1, X always has a last move
    """
    if board.count(' ') > 1:
        return False

    else:
        return True


def isWinner(b, l):
    """
        функция проверяет выиграшные комбинации и возвращает True или False

        Check all winner combinations (by row, by column, by diagonal)
        b for board , l for letter
    """
    return ((b[1] == l and b[2] == l and b[3] == l) or  # first row filled
            (b[4] == l and b[5] == l and b[6] == l) or  # second row filled
            (b[7] == l and b[8] == l and b[9] == l) or  # third row filled
            (b[1] == l and b[4] == l and b[7] == l) or  # first column
            (b[2] == l and b[5] == l and b[8] == l) or  # second column
            (b[3] == l and b[6] == l and b[9] == l) or  # third column
            (b[1] == l and b[5] == l and b[9] == l) or  # diagonal left top to right bottom
            (b[3] == l and b[5] == l and b[7] == l))  # diagonal right top to left bottom


def playerMove():
    run = True
    while run:
        move = input(
            'Пожалуйста введите число от 1 до 9 согласно позиции на игровом поле\n'+'-'*67+'\nPlease select a position to enter the X between 1 to 9 ---->  ')
        print('-' * 63)
        try:
            move = int(move)
            if 0 < move < 10:               # прием чисел от 1 до 9
                if spaceIsFree(move):       #  если есть свободное место на этой позиции заданой в move
                    run = False             #  передача хода компьютеру
                    insertLetter('X', move) #  заполнение ячейки Х'ом
                else:                       # если место занято вывод сообщения (run = True) продолжение хода
                    print(f'Извините, позиция {move} занята.\nSorry, space #{move} is occupied\n' + '-' * 63)
            else:                           # если ввод число не в диапозоне от 1 до 9
                print(' ' * 24 + 'Ошибка ввода \n' + ' ' * 24 + 'Type Error')
                print('-' * 63)
        except:         # вывод ошибки если ввод не число
            print(' ' * 24 + 'Только числа от 1 до 9 \n' + ' ' * 24 + 'Only numbers in range from 1 to 9')
            print('-' * 63)


def computerMove():
    # пронумеровываем наш лист board и проверяем еслм позиция не занята и индекс места не равен 0
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    # Check if computer move leads to win
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    # fill the corners first if available
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    # fill random corner from list of available corners
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # if there is no free corner fill center
    if 5 in possibleMoves:
        move = 5
        return move

    # if only edges available fill random cell in list of edges' cells
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print("Добро пожаловать в Игру! \nWelcome to the game!")
    printBoard(board)


    # Пока поле не заполнено
    while not(isBoardFull(board)):
        # если компьютер не выиграл ходит игрок, если выиграл стоп игра
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Ты с проиграл с позором! \n sorry you loose!")
            break

        # если игрок не выиграл ходит комп, если выиграл стоп игра
        if not (isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print("Ничья!\nTie game")
                break
            else:
                insertLetter('O', move)
                print('Я походил на позицию',move,'\ncomputer placed an O on position', move, ':')
                printBoard(board)
        else:
            print("Я проиграл человеку... Форматирую диск С:\ \nyou win!")
            break
        if isBoardFull(board):
            print("Ничья!\nTie game")



while True:
    x = input("-"*65+"\n Правила игры крестики-нолики уверен Вы знаете(если нет, гугл в помощь).\n\t\t\t Начнем-с? (y-да / n-нет)\n"+"-"*65+
        "\nRules are simple. Select a position where You want to place 'X'!\n But be careful. I am very clever!!! \n "
        "Do you want to try ? (y/n)\n\t\t")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    elif x.lower() == 'n':
        break
    else:
        print('Либо - Да(y) либо - Нет(n)\n I accept "y" or "n" only')
