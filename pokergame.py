import random
from collections import defaultdict, Counter

#Comparative value of starting hands in a poker game  
odds = [[-.09, -.14, -.12, -.12, -.12, -.12, -.12, -.12, -.12, -.13, -.13, -.14, -.15],
        [-.14, -.07, -.13, -.12, -.15, -.12, -.12, -.12, -.12, -.13, -.13, -.14, -.13],
        [-.12, -.13, -.03, -.12, -.12, -.12, -.12, -.12, -.12, -.13, -.13, -.13, -.12],
        [-.12, -.12, -.13, .02, -.12, -.11, -.15, -.12, -.12, -.13, -.13, -.13, -.12],
        [-.12, -.15, -.12, -.12, .07, -.15, -.15, -.12, -.11, -.12, -.13, -.12, -.12],
        [-.12, -.15, -.12, -.11, -.15, .16, -.15, -.10, -.10, -.15, -.15, -.11, -.10],
        [-.12, -.12, -.15, -.11, -.11, -.12, .25, -.10, -.10, -.10, -.11, -.11, -.07],
        [-.12, -.12, -.12, -.12, -.12, -.10, -.10, .38, -.07, -.09, -.08, -.07, -.03],
        [-.15, -.12, -.12, -.12, -.11, -.10, -.10, -.07, .58, -.03, -.02, .01, .08],
        [-.13, -.13, -.13, -.13, -.12, -.12, -.12, -.10, -.09, -.03, .86, .03, .08],
        [-.13, -.13, -.13, -.13, -.13, -.12, -.11, -.08, -.02, .03, 1.22, .16, .31],
        [-.14, -.14, -.13, -.13, -.12, -.11, -.11, -.07, .1, .08, .16, 1.67, .51],
        [-.15, -.13, -.12, -.12, -.12, -.10, -.07, -.03, .08, .19, .31, .51, 2.32]]

class pgame:

    def isstrt(self, l):
        l.sort(reverse=True)
        if (l[0][0]!=l[1][0]) and (l[1][0]!=l[2][0]) and (l[2][0]!=l[3][0]) and (l[3][0]!=l[4][0]) and (l[0][0]-l[4][0]==4):
            return l[0][0]
        elif (l[1][0]!=l[2][0]) and (l[2][0]!=l[3][0]) and (l[3][0]!=l[4][0]) and (l[4][0]!=l[5][0]) and (l[1][0]-l[5][0]==4):
            return l[1][0]
        elif (l[2][0]!=l[3][0]) and (l[3][0]!=l[4][0]) and (l[4][0]!=l[5][0]) and (l[5][0]!=l[6][0]) and (l[2][0]-l[6][0]==4):
            return l[2][0]
        else:
            return None

    def isflush(self, l):
        key = None
        key2 = None
        z = 0
        l.sort(reverse=True)
        l.sort(key=lambda x:x[1])
        for i in range(0,3):
            if l[i][1]==l[i+4][1]:
                z = 4
                if l[i][0]==(l[i+4][0]+4):
                    key= "sflush"   
                    if l[i][0]==13:
                        key="rflush"
                else:
                    if l[i][0]==13:
                        z = l[i][0]
                        if (2, z) in l and (3, z) in l and (4, z) in l and (5, z) in l:
                            key = "sflush"
                        else:
                            key = "flush"
                    else:
                        key = "flush"
            
                key2 = l[i][0]
                return key, key2
    
        return None

    def calchand(self, l):
        odds1 = odds[l[0][0]][l[1][0]]
        if odds1>0:
            return odds1
        else:
            return -1

    def calctight(self, l):
        odds1 = odds[l[0][0]][l[1][0]]
        if odds1 >.7:
            return odds1
        elif odds1> .2:
            return 0
        else:
           return -1

    def calcaggro(self, l):
        return odds[l[0][0]][l[1][0]]+.3

    def calcbluff2(self, l, raises):
        if raises==true and  odds[l[0][0]][l[1][0]] > .4:
            return odds[l[0][0]][l[1][0]]

    def calcbluff(self, l):
        odds1 = odds[l[0][0]][l[1][0]]
        if odds1 < -.1:
            return odds1*(-5)
        else:
            return odds1

    def calcboard(self, l):
        s = 0
        l.sort(key=lambda x:x[1])
        flush = False
        if l[0][1]==l[4][1]:
            flush == True
        l.sort(reverse=True)
        l2 = []
        for i in range(0, 5):
            l2.append(l[i][0])
        result = [item for items, c in Counter(l2).most_common() 
                                      for item in [items] * c] 
        if result[0]==result[4]:
            return max(l)[0]*100000000000000 + l[0][0]
        elif (result[0]==result[2]) and (result[3]==result[4]):
            return result[0]*1000000000000 + l[0][0]
        elif flush == True:
            return max(l)[0]*10000000000+l[0][0]
        elif (l[0][0]!=l[1][0]) and (l[1][0]!=l[2][0]) and (l[2][0]!=l[3][0]) and (l[3][0]!=l[4][0]) and (l[0][0]-l[4][0]==4):
            return max(l)[0]*100000000+l[0][0]
        elif result[0]==result[2]:
            return result[0]*1000000+l[0][0]
        elif (result[0]==result[1]) and (result[2]==result[3]):
            return result[0]*10000 + result[2]
        elif (result[0]==result[1]):
            return result[0]*100+l[0][0]
        else:
            return max(l)[0]
    
    def pairs(self, l):
        l.sort(reverse=True)
        l2 = []
        for i in range(0, 7):
            l2.append(l[i][0])
        result = [item for items, c in Counter(l2).most_common() 
                                          for item in [items] * c] 
        return result

    def calcscore(self, winner):
        s1 = 0
        pair = self.pairs(winner)
        if(pair[0]==pair[3]):
            s1+=pair[0]*100000000000000 #four
        elif pair[0]==pair[2]: 
            if pair[3]==pair[4]:
                s1+=pair[0]*1000000000000 #full house
            else:
                s1+=pair[0]*1000000 #3
        elif pair[0]==pair[1]:
            if pair[2]==pair[3]:
                s1+=pair[0]*10000+pair[2]*100  #2
            else:
                s1+=pair[0]*100    #single pair
        tflush = self.isflush(winner)
        if tflush is not None and s1< 10000000000:
            s1=0
            if tflush == "flush":
                s1+=10000000000*max(winner)
            elif tflush == "sflush":
                s1+=10000000000000000*max(winner)
        str1 = self.isstrt(winner)
        if str1 != None and s1 < 100000000:
            s1=0
            s1 += str1*100000000
        s1+=max(winner)[0]
        return s1

    def calcscore2(self, l):
        if l[0][0]==l[1][0]:
            return min(100, 50+l[0][0]*3)
        else:
            return max(l[0][0],l[1][0])    

    def calcchoice(self, player, pot, newbet, order):

        choice1 = odds[player.hand[0][0]-2][player.hand[1][0]-2] #choice1 is designed to be a rational calculation of odds to win
        choice = choice1*player.grid[0]+ player.grid[3]-pot*player.grid[1]*.1+.1*order*player.grid[2]
        if choice < 0:
            return -1
        choice = choice1*player.grid[4]+ player.grid[5]-pot*player.grid[6]*.1+order*.1*player.grid[7]
        if choice <.5:
            return 0
        else:
            return min(10, choice)
        return choice

    def game(self, plist, players):
        list = [(2, 'S'), (2, 'H'), (2, 'D'), (2, 'C'),(3, 'S'), (3, 'H'), (3, 'D'), (3, 'C'),
        (4, 'S'), (4, 'H'), (4, 'D'), (4, 'C'),(5, 'S'), (5, 'H'), (5, 'D'), (5, 'C'),(6, 'S'), (6, 'H'), (6, 'D'), (6, 'C'),
        (7, 'S'), (7, 'H'), (7, 'D'), (7, 'C'),(8, 'S'), (8, 'H'), (8, 'D'), (8, 'C'),(9, 'S'), (9, 'H'), (9, 'D'), (9, 'C'),
        (10, 'S'), (10, 'H'), (10, 'D'), (10, 'C'),(10, 'S'), (10, 'H'), (10, 'D'), (10, 'C'),(11, 'S'), (11, 'H'), (11, 'D'), (11, 'C'),
        (12, 'S'), (12, 'H'), (12, 'D'), (12, 'C'),(13, 'S'), (13, 'H'), (13, 'D'), (13, 'C'), (14, 'S'),
        (14, 'H'), (14, 'D'), (14, 'C')]
        for p in range(0, len(plist)):
            plist[p].hand=[]
        winner2=[]
        board = []
        scores = []
        amountbet = [0 for _ in range(players)] 
        choice = [0 for _ in range(players)] 
        nbets = 0
        totalbets = -1
        s1=s2=0
        pot = 0
        r = plist[0].money+plist[1].money
        bsize = 10
        nump = len(plist)
        for i in range(len(plist)):
            plist[i].hand.append(list.pop(random.randrange(0,len(list))))
            plist[i].hand.append(list.pop(random.randrange(0,len(list))))
        plist[0].prob = self.calcscore2(plist[0].hand)
        plist[1].prob = self.calcscore2(plist[1].hand)
        for i in range(0, len(plist)):
            plist[i].ingame = 1
        counter = len(plist)
        while counter>0 and nump > 1: #in other words, someone has raised
            for p in range(0, players):
                if plist[p].ingame==0:
                    continue
                if (p == 0) and (totalbets < 0):
                    amountbet[0]=10
                    pot = 10
                    bsize = 10
                    counter -= 1
                    totalbets+=1
                else:
                    if p==0:
                        order = 1
                    else:
                        order = 0
                    choice = int(self.calcchoice(plist[p], pot, bsize-amountbet[p], order))
                    if choice == -1:
                        plist[p].ingame=0
                        counter -=1
                        nump -= 1
                        if counter == 0:
                            break
                    elif choice != 0 and totalbets < 3:
                        counter = nump-1
                        bsize+=choice
                        totalbets+= 1
                        nbets = 0
                        pot+= bsize-amountbet[p]
                        amountbet[p]=bsize
                    else:
                        pot += bsize-amountbet[p]
                        amountbet[p]=bsize
                        counter -= 1
                        if counter==0:
                            break
        if nump < 2:
            for i in range(0, len(plist)):
                if plist[i].ingame==1:
                    winner = i
                    plist[i].money+=pot
                plist[i].money-=amountbet[i]
   #             print(plist[i].money)
    ##    print("pot")
     #   print(pot)
     #   print("amount bet")
     ##   print(amountbet[0])
      #  print("money")
       # for i in range(0, len(plist)):
      #      print(plist[i].money)

            return
        else:
            for i in range(0, 5):  
                n = list.pop(random.randrange(0, len(list)))
                board.append(n)
                for j in range(0, len(plist)):
                    plist[j].hand.append(n)
            for j in range(0, len(plist)):
                scores.append(self.calcscore(plist[j].hand))
        zzz = scores.index(max(scores))
        for i in range(0, len(plist)):
            plist[i].money-=amountbet[i]
    #plist[zzz].money+=pot
        pval = self.calcboard(board)
    #print(s1)
    #print(s2)
    #print(p1.hand)
    #print(pval)
        plist[zzz].money+=pot
    #print(plist[zzz].money)
    #print("is the winner")
    #print(pot)
    #print("is the pot")
