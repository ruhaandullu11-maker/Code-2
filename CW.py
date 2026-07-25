import random
import time

# Rules explained to the player
print('Welcome to the Card game of War')
print('Fight for 52 turns and who ever has more cards at the end wins!')  # 52 turns like the number of cards in a deck

# Creating the list for the deck of cards
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']             
suits = ['c', 'd', 'h', 's']     



deck = [] 
# Creating the deck of cards by joining the suits and cards
for ss in range(len(suits)):
    for cc in range(len(cards)):
        deck.append(suits[ss]+cards[cc])

# Printing the joined deck of cards
print('Unshuffled Deck:')
for ss in range(len(deck)):
    print(deck[ss], end = ' ')
print()
print()

# Shuffling the deck of cards
random.shuffle(deck) 

print('Shuffled Deck:')
for ss in range(len(deck)):
    print(deck[ss], end = ' ')


# Tossing the coin to decide who goes first
toss = random.choice(deck)
print()
print('Tossing the coin ...')
if toss[0] == 'c' or toss[0] == 'd':
    first_mover = 'player'
    print('You won the toss')
else:
    first_mover = 'cpu'
    print('Cpu won the toss')


# Distributing 26 cards to the player and 26 to the CPU
playercards = deck[0:26:1]
cpucards = deck[26:52:1]
tablecards = []


movecomp = False
gamecomp = False
movesplayed = 0

while not(gamecomp):

  movecomp = False

  if len(playercards)<1 or len(cpucards)<1:
    movecomp = True
    gamecomp = True

  while not(movecomp):           # First move
    cardofpla = playercards.pop(0)
    cardofcpu = cpucards.pop(0)
    print()
    print('Player Card is ...', cardofpla)
    print('Computer Card is ...', cardofcpu)


    tablecards.append(cardofpla)
    tablecards.append(cardofcpu)
    
    # Determines winner of first move
    if cards.index(cardofpla[1])>cards.index(cardofcpu[1]):
      print('Player Wins ... ')
      input()
      playercards.extend(tablecards)
      tablecards.clear()
      movecomp = True
      movesplayed = movesplayed + 1
    elif cards.index(cardofpla[1])<cards.index(cardofcpu[1]):
      print('CPU Wins ... ')
      input()
      cpucards.extend(tablecards)
      tablecards.clear()
      movecomp = True
      movesplayed = movesplayed + 1
    # If its a draw the war begins
    else:
      print("War begins")
      input()
      # Checking if there is enough cards to play the war
      if len(playercards)<4 or len(cpucards)<4:
        movecomp = True
             
      else:
              
        tablecards.extend(playercards[0:3])
        tablecards.extend(cpucards[0:3])

                        
        del playercards[0:3]
        del cpucards[0:3]
    # Checking if the game is complete
    if movesplayed == 52:
      gamecomp = True

    print("Player Cards:", len(playercards), "CPU Cards:", len(cpucards), "Table Cards:", len(tablecards))    


print()
print()
print()

 # Determines the winner of the game
if len(playercards) > len(cpucards):
  print('Player is the winner')

elif len(playercards) < len(cpucards):
  print('CPU is the winner')

# If its a draw the winner gets settled by a coin toss
else: 
  print('Draw...so it will be settled with a coin toss')
  toss = random.choice(deck)
  print()
  print('Tossing the coin ...')
  if toss[0] == 'c' or toss[0] == 'd':
      winner = 'player'
      print('And its...player thast wins the game!!')
  else:
      winner = 'cpu'
      print('And its...CPU that wins the game!!')