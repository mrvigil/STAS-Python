from readchar import readchar
import random, time
keyboardPOS = {
    "q": 1,
    "a": 2,
    "z": 3,
    "w": 4,
    "s": 5,
    "x": 6,
    "e": 7,
    "d": 8,
    "c": 9,
    "r": 10,
    "f": 11,
    "v": 12,
    "t": 13,
    "g": 14,
    "b": 15,
    "y": 16,
    "h": 17,
    "n": 18,
    "u": 19,
    "j": 20,
    "m": 21,
    "i": 22,
    "k": 23,
    "o": 24,
    "l": 25,
    ".": 26,
    "p": 27,
    ";": 28,
    "/": 29
}
keyboard = [
    "q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v", "t", "g", "b",
    "y", "h", "n", "u", "j", "m", "i", "k", "o", "l", ".", "p", ";", "/"
]
line = []

print('\033c')


def printtarget(position):
    target=['*****']
    
    print('\033c')
    print()
    for i in range(0, position*2-2):
        target.insert(0, "")
    for i in target:
        print(i)
    print()
    for i in range(0, 19):
        print()
    for i in keyboard:
        print(i)
    print()
    target.clear()


def printscreen(input,position):
    target = ['*****']
    print('\033c')
    print()
    if keyboardPOS[input]-position < 3 and keyboardPOS[input]-position > -1 :
      target=['OOOOO']
    for i in range(0, position*2-2):
        target.insert(0, "")
    for i in target:
        print(i)
    print()
    for i in range(1, keyboardPOS[input]):
        line.append(" ")
    line.append(input)
    for i in range(0, 19):
        for i in line:
            print(i)
        print()
    for i in keyboard:
        print(i)
    print()
    line.clear()


print()
for i in range(0, 19):
    print()
for i in keyboard:
    print(i)
print()
while True:
  position = random.randint(0, 29)
  printtarget(position)
  printscreen(readchar(), position)
  time.sleep(.15)
