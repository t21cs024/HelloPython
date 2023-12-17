'''
Created on 2023/10/13

@author: t21cs024
'''
'''
Created on 2023/10/13

@author: t21cs024
'''

import random

def rps(te):
    if te == 0:
        return "グー"
    elif te == 1:
        return "チョキ"
    else:
        return "パー"
    
def shouhai(a,b):
    if(a == b):
        return "引き分け"
    elif (a != 2 and a < b) or (a == 2 and b == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"

def janken():
    anote = random.randint(0, 2)
    bnote = random.randint(0, 2)
    print("Aの手：" + rps(anote) + " v.s. " + "Bの手：" + rps(bnote) )
    
    if(anote == bnote):
        print (" → 引き分け")
        return 0
    elif (anote != 2 and anote < bnote) or (anote == 2 and bnote == 0):
        print(" →  Aの勝ち")
        return 1
    else:
        print(" → Bの勝ち")
        return 2
    
def three_janken():
    aWin = 0
    bWin = 0
    if janken() == 1:
        aWin += 1
    elif janken() == 2:
        bWin += 1
    
janken()
    
    
    
    
    
    