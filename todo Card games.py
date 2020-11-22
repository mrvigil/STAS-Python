import random
def poker():
  values = ["Ace", "King", "Queen", "Jack", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
  suits = ["_of_Hearts", "_of_Diamonds", "_of_Clubs", "_of_Spades"]
  cards = []
  hand=[]
  for x in suits:
      for y in values:
        cards.append(y + x)
  for x in range(0, 5):
    hand.append(cards.pop(random.randint(0,len(cards)-1)))
  print(hand)
def uno():
  values = ["Draw 2", "Draw 4", "Reverse", "Skip", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
  suits = ["_red_", "_green_", "_blue_", "_yellow_"]
  cards = []
  hand=[]
  for x in suits:
      for y in values:
        cards.append(x + y)
  for x in range(0, 5):
    hand.append(cards.pop(random.randint(0,len(cards)-1)))
  print(hand)
