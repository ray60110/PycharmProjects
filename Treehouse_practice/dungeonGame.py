import random
import sys
import os

squares=[(0, 4), (1,4), (2, 4), (3, 4), (4, 4),
         (0, 3), (1,3), (2, 3), (3, 3), (4, 3),
         (0, 2), (1,2), (2, 2), (3, 2), (4, 2),
         (0, 1), (1,1), (2, 1), (3, 1), (4, 1),
         (0, 0), (1,0), (2, 0), (3, 0), (4, 0),]


def get_location():
      # to create a random position of monster player door.
      # try to prevent either two of the object were created at
      # the same spot!

      # input is random created, output is feasible location of
      # three tuple, which we can assign them with muti-assignment
      
      monster= random.choice(squares)
      start= random.choice(squares)
      door= random.choice(squares)
      if monster == door or monster == start or start== door:
            return get_location()
      else:
            return monster, start, door

def get_moves(player):
      # to get feasible direction of our characher can go.
      # input is player's position and output is a list of feasible
      # direction.
      
      moves=['left', 'right', 'up', 'down']
      if player[0]==0:
            moves.remove('left')
      if player[1]==4:
            moves.remove('up')
      if player[0]==4:
            moves.remove('right')
      if player[1]== 0:
            moves.remove('down')
      return moves

def clear():
      # a function that can clear the screen.
      return os.system('cls')

def draw_map():
      # to use a visualized picture to show the position for player
      # no need to return value but print the map.
      print(' _ _ _ _ _')
      tile='|{}'

      for inx, cell in enumerate(squares):
            if inx not in [4, 9, 14, 19, 24]:
                  if cell == player:
                        print(tile.format('x'), end='')
                  else:
                        print(tile.format('_'), end='')
            else:
                  if cell == player:
                        print(tile.format('x|'))
                  else:
                        print(tile.format('_|'))


def move_player(player, move):
      # input is user's input and player
      x, y = player
      
      if move.lower()== 'up':
            y+=1
      elif move.lower()== 'down':
            y-=1
      elif move.lower()== 'left':
            x-=1
      elif move.lower()== 'right':
            x+=1
      return x, y


monster, player, door= get_location()
game= True

while game:
      moves= get_moves(player)
      # list for move
      print('Welcome to this dungeon game!')
      print('You are currently in {}'.format(player))
      print('You can move {} directions.'.format(moves))
      print("please press 'QUIT' to leave")
      
      draw_map()
      # draw a first map

      move= input("> ")

      if move.lower()== 'quit':
            sys.exit()
      if move in moves:
      # means its a feasible move.
            player= move_player(player, move)
            # put player's location and user's input to bring back position.
      
      else:
            print('You cannot do that!')
            continue
      #defin what is good move and what is bad move!
      
      if player == door:
            print('Congrat! You survie!')
            break
      elif player == monster:
            print('Sorry, you are dead, eaten by a monster')

            retry= input("Play again? (Y/n)")
            if retry != 'n':
                  continue
            else:
                  game= False
                  
      
