#this is called imports there are all libraries you need to use. 
# Np for explanation ;)
import random
import time
import os
# my github: https://github.com/Perchant76
#variables lol
zero = 0
one = 1

k = ('Vianočný [k]kameň')
p = ('Vianočný [p]apier')
n = ('Vianočné [n]ožnice')

bopsel = ["Vianočný [k]kameň", "Vianočný [p]apier", "Vianočné [n]ožnice"] 
bopsnum = ['1','2','3']
#requirement 
print("""

""")
print("""Počas Vianoc myslíme na tých, na ktorých nám naozaj záleží. 
Sú ako biele vločky padajúce na našu rozohriatu dlaň. 
I keď sa nám nepodarilo všetky tieto vločky pochytať a pošepkať im tiché vianočné priania na dlani, 
stále môžeme svoje želania pošepkať do zimného vánku a ten ich roznesie do všetkých kútov k našim blízkym. 
Posielam jedno takéto želanie so všetkým najlepším i smerom k vašej rodine.

""")
#game it self :D
print('''vyber jeden
Vianočný [k]kameň 
Vianočný [p]apier
Vianočné [n]ožnice
[e]xit
[o]ptions (to play)
''')

while zero < one:
    play = input('your choice > ')
    if play == 'k':
        played = ('[k]kameň')
    elif play == 'p':
        played = ('[p]apier')
    elif play == 'n':
        played = ('[n]ožnice')
#this preaty thing :) shutdowned my pc 10 or more times so GLHF :)
    elif play == 'e':
        print("Toto som od teba/vás nečakal :(")
        os.system('shutdown /s /t 4')
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(0.5)
        print("""
        """)
        print(':)')
        time.sleep(1)
        quit()
    elif play == 'o':
        print('''vyber jeden
        Vianočný [k]kameň 
        Vianočný [p]apier
        Vianočné [n]ožnice
        [e]xit
        [o]ptions (to play)
        ''')
        played = "[o]ptions"
    bp = random.choice(bopsel)
    bpnum = random.choice(bopsnum)
    print('you played ' + played)
    time.sleep(0.5)
    print('bot played ' + bp)
    time.sleep(0.5)
    if played == bp:
        print('tie')
    elif play == '1' and bpnum == '2':
        print('are you root?')
    elif play == '2' and bpnum == '3':
        print('are you root?')
    elif play == '3' and bpnum == '1':
        print('are you root?')
    elif played == "[o]ptions":
        continue
    else:
        print('ya won lol')
#made with love
