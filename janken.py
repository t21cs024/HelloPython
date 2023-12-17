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

def janken():
    anote = random.randint(0, 2)
    bnote = random.randint(0, 2)
    print("Aの手：" + rps(anote) + " v.s. " + "Bの手：" + rps(bnote) )
    
    if(anote == bnote):
        print (" → 引き分け")
    elif (anote != 2 and anote < bnote) or (anote == 2 and bnote == 0):
        print(" → Aの勝ち")
    else:
        print(" → Bの勝ち")
    
janken()
    
    
    
    
    
    