import random
print("Hello World!")
while True:
  answer=input("Do you want to play a game?")
  win=0
  if answer.upper()=='NO':
    print("that's too bad -Good bye!")
    break
  elif answer.upper()=='YES':
    print("Good, I'm thinking of a number between 1 and 100.")
    print("You only have 6 tries.")
    number=random.getrandbits(7)
    for i in range(1,7):
      answer=int(input("?"))
      if answer==number:
        print("You guessed it!")
        win=1
        break
      elif answer > number:
        print(answer," is to high")
      elif answer < number:
        print(answer," is to low")
      print("You have ", 6-i, " tries left")