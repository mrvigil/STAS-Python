snowman1=[
'       _________        ' ,
'      /         \       ' ,
'      |  x   x  |      ' ,
' __   |    v    |  __  ' ,
'   \  \_________/ /     ',
'    \ /    O    \/      ' ,
'      |    O    |      ' ,
'      |    O    |      ' ,
'      \_________/       ']

snowman2=[
'       _________        ' ,
'      /         \       ' ,
'      |  x   x  |      ' ,
' __   |    v    |  __  ' ,
'   \  \_________/ /     ',
'    - /    O    \-      ' ,
'      |    O    |      ' ,
'      |    O    |      ' ,
'      \_________/       ']

snowman3=[
'       _________        ' ,
'      /         \       ' ,
'      |  x   x  |      ' ,
'      |    v    |    ' ,
'  /-  \_________/ --\   ',
'    \ /    O    \/      ' ,
'      |    O    |      ' ,
'      |    O    |      ' ,
'      \_________/       ']
snowmen=[snowman1, snowman2, snowman3]
import time
print()
for x in range(0,len(snowmen)):
  for y in range(0, len(snowmen[x])):
    print(snowmen[x][y])
  time.sleep(.25)
  print('\033c')


