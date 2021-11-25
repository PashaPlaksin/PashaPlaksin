board = list(range(1,10))

def take_input(current_user):
   valid_input = False
   while not valid_input:
      answer = input("Куда поставим " + current_user+": ")
      if not answer.isdigit():
         print ("Введите число")
         continue
      answer = int(answer)
      if answer >= 1 and answer <= 9:
         if (str(board[answer-1]) not in "XO"):
             board[answer-1] = current_user
             valid_input = True
         else:
             print("Клетка занята")
      else:
        print("Необходимо ввести число от 1 до 9")

def check_win(board):
   winning_situations = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

   for i in winning_situations:
       if board[i[0]] == board[i[1]] == board[i[2]]:
          return board[i[0]]
   return False

def boards(board):
   for cell in range(3):
      print (board[0+cell*3], " ", board[1+cell*3], " ", board[2+cell*3])

counter = 0
win = False
while not win:
    boards(board)
    if counter % 2 == 0:
       take_input("X")
    else:
       take_input("O")
    counter += 1
    if counter > 4:
       status = check_win(board)
       if status:
          print("Выиграл " + status)
          win = True
          break
    if counter == 9:
        print ("Ничья!")
        break
