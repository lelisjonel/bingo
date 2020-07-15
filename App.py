import random
                    


def play():
    letters = ['B','I','N','G','O']
    bingo = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45],
    [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60],
    [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]]
    limit = [0,0,0,0,0]
    for turn in range(76):
        game = input('"Press Enter to Roll"').upper()
        if not turn == 75:
            if game == '':
                select_letter = random.choice(letters)
                if select_letter == 'B':
                    select_number =  random.choice(bingo[0])
                    bingo[0].remove(select_number)
                    limit[0] += 1
                    if limit[0] == 15:
                        letters.remove('B')
                elif select_letter == 'I':
                    select_number = random.choice(bingo[1])
                    bingo[1].remove(select_number)
                    limit[1] += 1
                    if limit[1] == 15:
                        letters.remove('I')
                elif select_letter == 'N':
                    select_number = random.choice(bingo[2])
                    bingo[2].remove(select_number)
                    limit[2] += 1
                    if limit[2] == 15:
                        letters.remove('N')
                elif select_letter == 'G':
                    select_number = random.choice(bingo[3])
                    bingo[3].remove(select_number)
                    limit[3] += 1
                    if limit[3] == 15:
                        letters.remove('G')
                elif select_letter == 'O':
                    select_number = random.choice(bingo[4])
                    bingo[4].remove(select_number)
                    limit[4] += 1
                    if limit[4] == 15:
                        letters.remove('O')
                print(f'''
                	{turn + 1}: Sa letrang {select_letter} = "{select_number}"

                    ''')
            else:
                print('Just Press Enter Only!')
        elif turn == 75:
            print('END OF GAME ^_^ THANK YOU!!!')
            another_game = input('Play Again?: Y/N ')
            if another_game == 'Y':
                start()
            else:
                print('Bye!')
                          


def start():
    want_to_play = input('Want to Play Y/Q: ').upper()
    if want_to_play == 'Y':
        play()
    elif want_to_play == 'Q':
        print('Bye!')
    else:
        print(f'''
        Type "Y" to Play..
        Type "Q" to Quit!
        ''')

print('''
        "Welcome to Bingo!"
        Version: 1.0 
        Author: Jonel Lelis

''')
name = input('What is your name? ')
print(f'Hello {name}! thank you for choosing this bingo app')
start()


