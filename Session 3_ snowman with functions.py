def drawsnowman(pic):
    if pic == 1:
      print("")
      print("      _______       ")
      print("    /        \       ")
      print("    |        |     ")
      print("     \______/      ")
      print("     /      \        ")
      print("    |        |     ")
      print("     \______/     ")
      print("")    
    elif pic == 2:
      print("")
      print("      _______       ")
      print("    /  x  x  \       ")
      print("    |        |     ")
      print("     \______/      ")
      print("     /      \        ")
      print("    |        |     ")
      print("     \______/     ")
      print("")    
    elif pic == 3:   
      print("")
      print("      _______       ")
      print("    /  x  x  \       ")
      print("    |    v   |     ")
      print(" _   \______/     ")
      print("   \ /      \        ")
      print("    |        |     ")
      print("     \______/     ")
      print("")    
    elif pic == 4:  
      print("")
      print("      _______       ")
      print("    /  x  x  \       ")
      print("    |    v   |     ")
      print(" _   \______/  _   ")
      print("   \ /   8  \ /      ")
      print("    |    8   |     ")
      print("     \______/     ")
      print("")    
 
import time
for i in range(1,5):
  print('\033c')
  drawsnowman(i)
  time.sleep(.5)
import random
words = ["apple", "dog", "pizza", "boy"]
win = False
word = words[random.randint(0, len(words) - 1)]
guessed = []
display = []
for i in range(0, (len(word))):
    display.append("_")
print("Start guessing!!!!!")
print(display)
while win == False:
    guess = input("Guess a letter...")
    for x in range(len(word)):
        if guess in word[x]:
            display[x] = guess
        print(display[x], end=" ")
    if guess not in word:
        print("Not in word!!!")
        guessed.append(guess)
        print("Here is what you've already guessed: ")
        print(guessed)
        drawsnowman(len(guessed))
    else:
        print("That letter was in the word")
    if '_' not in display:
        print("YOU WIN!!!!")
        win = True
    if len(guessed)==4:
      print("Too bad-you lose")
      break
