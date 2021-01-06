import random

class Game:
  def __init__(self):
    self.p1letter = ''
    self.p2letter = ''
    self.theBoard = [' '] * 10
    self.p1name = ''
    self.p2name = ''
  
  def __repr__(self):
    return 'game object\nnot sure if I should exist...'
    # this function shouldn't be called.
  
  def Letters(self):
    self.p1letter = ''
    while not (self.p1letter == 'X' or self.p1letter == 'O'):
        print('Player 1: Do you want to be X or O?')
        self.p1letter = input().upper()

    #Sets player two's letter
    if self.p1letter == "X":
        self.p2letter = "O"
    elif self.p1letter == "O":
        self.p2letter = "X"
  
  def Names(self):
    self.p1name = input('Alright, Player 2 you are {}.\nWhat is your name, Player 1? '.format(self.p2letter))
    self.p2name = input('What is your name, Player 2? ')
  
  def SetUp(self):
    self.Letters()
    self.Names()
    return self.p1letter, self.p2letter, self.theBoard, self.p1name, self.p2name

class Player:
    def __init__(self, letter, nameOfPlayer, nameOfOpponent):
      
        self.letter = letter
        self.name = nameOfPlayer
        self.nameOfOpponent = nameOfOpponent
        self.move = ''
        self.wantsPlayAgain = True
    


    def __repr__(self):
        return self.name

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return self.name
        else:
            return self.nameOfOpponent

    def isSpaceFree(self, board, move):
        return board[move] == ' '
    
    #Gets player move
    def getMove(self, board):
        self.move = ''
        #Makes sure it is a number 1-9
        numbers1_9 = [1,2,3,4,5,6,7,8,9]
        while self.move not in numbers1_9:
          #Trys to get value
          try:
            self.move = int(input('Where would you like to go {}?:'.format(self.name)))
            move = self.move
            if not self.isSpaceFree(board, move):
              print('Sorry {} that move is not avalible. Please enter a number between 1-9'.format(self.name))
              self.move = 'NONE'

          #If there is a failure to turn into int 
          #Then they must have not entered a number
          except:
            print('Error: Please enter a number between 1-9')
          
    def makeMove(self, board):
      move = self.move
      if self.isSpaceFree(board, move):
        board[self.move] = self.letter
        self.drawMove(board)
      elif not self.isSpaceFree(board, move):
        print('Sorry {} that move is not avalible.'.format(self.name))

    def drawMove(self, board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' +
              board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' +
              board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' +
              board[3])
        print('   |   |')
    
    def isWinner(self, bo, le):
      # Given a board and a player's letter, this function returns True if that player has won.
      # We use bo instead of board and le instead of letter so we don't have to type as much.
      return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
          (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
          (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
          (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
          (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
          (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
          (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
          (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
    
    def isBoardFull(self, board):
      # Return True if every space on the board has been taken. Otherwise return False.
      for i in range(1, 10):
          if self.isSpaceFree(board, i):
            return False
      return True

    def playAgain(self,theBoard):
      # This function returns True if the player wants to play again, otherwise it returns False.
      play_again = ''
      while not play_again == 'yes' or play_again == 'no':
        print('Do you want to play again? (yes or no)')
        play_again = input().lower()
        if play_again.startswith('y'):
          self.wantsPlayAgain = True
          theBoard = [' '] * 10
          return theBoard
        elif play_again.startswith('n'):
          self.wantsPlayAgain = False
          print('Thanks for Playing!')
          break
      



print('Welcome to Tic Tac Toe!')



  #sets the game up

theGame = Game()
player1_letter, player2_letter, theBoard, player1_name, player2_name = theGame.SetUp()

#Class(letter, nameOfPlayer, nameOfOpponent)
Player1 = Player(player1_letter, player1_name, player2_name)
Player2 = Player(player2_letter, player2_name, player1_name)

  #Tells who goes first
turn = Player1.whoGoesFirst()
print('The player ' + turn + ' will go first.')


#game starts here
while Player1.wantsPlayAgain == True:
  gameIsPlaying = True
  Player1.drawMove(theBoard)
  while gameIsPlaying == True:
    if turn == Player1.name:
      Player1.getMove(theBoard)
      Player1.makeMove(theBoard)
      if Player1.isWinner(theBoard, player1_letter):
          print('Hooray {}! You have won the game!'.format(Player1))
          gameIsPlaying = False
      else:
        if Player1.isBoardFull(theBoard):
          print('The game is a tie!')
          gameIsPlaying = False
        else: 
          turn = Player2.name 
    elif turn == Player2.name:
      Player2.getMove(theBoard)
      Player2.makeMove(theBoard)
      if Player2.isWinner(theBoard, player2_letter):
          print('Hooray {}! You have won the game!'.format(Player2))
          gameIsPlaying = False
      else:
        if Player1.isBoardFull(theBoard):
          print('The game is a tie!')
          gameIsPlaying = False
        else: 
          turn = Player1.name

  theBoard = Player1.playAgain(theBoard)
