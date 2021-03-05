import random, itertools, time, copy, sys, score
from pokergame import pgame
from collections import defaultdict, Counter
population=[]
players = 2
psize = 100 #population size
gens = 50 #number of generations
ngames = 10000
valList = []
zzzz = 0
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
class player:
    def __init__(self, grid, hand):
        self.grid = grid
        self.wins = 0
        self.hand=hand
        self.money=200
        self.ingame= 1

def isstr(l):
    l.sort(reverse=True)
    if (l[0][0]!=l[1][0]) and (l[1][0]!=l[2][0]) and (l[2][0]!=l[3][0]) and (l[3][0]!=l[4][0]) and (l[0][0]-l[4][0]==4):
        return l[0][0]
    elif (l[1][0]!=l[2][0]) and (l[2][0]!=l[3][0]) and (l[3][0]!=l[4][0]) and (l[4][0]!=l[5][0]) and (l[1][0]-l[5][0]==4):
        return l[1][0]
    elif (l[2][0]!=l[3][0]) and (l[3][0]!=l[4][0]) and (l[4][0]!=l[5][0]) and (l[5][0]!=l[6][0]) and (l[2][0]-l[6][0]==4):
        return l[2][0]
    else:
        return None

def isflush(l):
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

def calchand(l):
    odds1 = odds[l[0][0]][l[1][0]]
    if odds1>0:
        return odds1
    else:
        return -1

def calctight(l):
    odds1 = odds[l[0][0]][l[1][0]]
    if odds1 >.7:
        return odds1
    elif odds1> .2:
        return 0
    else:
       return -1

def calcaggro(l):
    return odds[l[0][0]][l[1][0]]+.3

def calcbluff2(l, raises):
    if raises==true and  odds[l[0][0]][l[1][0]] > .4:
        return odds[l[0][0]][l[1][0]]

def calcbluff(l):
    odds1 = odds[l[0][0]][l[1][0]]
    if odds1 < -.1:
        return odds1*(-5)
    else:
        return odds1

def calcboard(l):
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
    

def pairs(l):
    l.sort(reverse=True)
    l2 = []
    for i in range(0, 7):
        l2.append(l[i][0])
    result = [item for items, c in Counter(l2).most_common() 
                                      for item in [items] * c] 
    return result

def calcscore(winner):
    s1 = 0
    pair = pairs(winner)
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
    tflush = isflush(winner)
    if tflush is not None and s1< 10000000000:
        s1=0
        if tflush == "flush":
            s1+=10000000000*max(winner)
        elif tflush == "sflush":
            s1+=10000000000000000*max(winner)
    str1 = isstr(winner)
    if str1 != None and s1 < 100000000:
        s1=0
        s1 += str1*100000000
    s1+=max(winner)[0]
    return s1

def calcscore2(l):
    if l[0][0]==l[1][0]:
        return min(100, 50+l[0][0]*3)
    else:
        return max(l[0][0],l[1][0])    

def calcchoice(player, pot, newbet, order):

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

def games(plist):
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
    plist[0].prob = calcscore2(plist[0].hand)
    plist[1].prob = calcscore2(plist[1].hand)
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
                choice = int(calcchoice(plist[p], pot, bsize-amountbet[p], order))
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
        return
    else:
        for i in range(0, 5):  
            n = list.pop(random.randrange(0, len(list)))
            board.append(n)
            for j in range(0, len(plist)):
                plist[j].hand.append(n)
        for j in range(0, len(plist)):
            scores.append(calcscore(plist[j].hand))
    zzz = scores.index(max(scores))
    for i in range(0, len(plist)):
        plist[i].money-=amountbet[i]
    #plist[zzz].money+=pot
    pval = calcboard(board)
    #print(s1)
    #print(s2)
    #print(p1.hand)
    #print(pval)
    plist[zzz].money+=pot
    #print(plist[zzz].money)
    #print("is the winner")
    #print(pot)
    #print("is the pot")

        
def testfitness(population):
    global players
    for i in range(0, ngames):   #games per run
        random.shuffle(population)
        k = 0
        for j in range(0, int(psize/players)):
            nlist=[]
            for m in range(0, players):
                nlist.append(population[k])
                k+= 1
            pgame().game(nlist, players)
def mutation(b): 
    for i in range(0, 4): #0, .25
        mutChance = random.randint(0,50)
        if mutChance < 1:
            z = random.gauss(0, .10)
            b.grid[i] = b.grid[i] + z
            
    for i in range(4,8):
        mutChance = random.randint(0,50)
        if mutChance < 1:
            z = random.gauss(0, .1)
            b.grid[i] = b.grid[i] + z
    return b
            
def crossingover(best1, best2):
    poss= random.randint(0, 10)
    if poss < 7:
        wgrid = best1.grid[:]
        z = random.randint(0,3)
        z2=random.randint(-2,4)
        best1.grid[z2:z2+z] = best2.grid[z2:z2+z]
        best2.grid[z2:z2+z]=wgrid[z2:z2+z]
    return best1, best2
def tournament(population):
    for i in range(0, len(population)):
        w = random.sample(population, 3)
        if (w[0].money> w[1].money) and (w[0].money>w[2].money):
            best = w[0]
        elif (w[1].money> w[2].money) and (w[1].money>w[0].money):
            best = w[1]
        else:
            best = w[2]
        w2 = random.sample(population, 3)
        if w2[0].money> w2[1].money and w2[0].money>w2[2].money:
            best2 = w[0]
        elif w2[1].money> w2[2].money and w2[1].money>w2[0].money:
            best2 = w2[1]
        else:
            best2 = w2[2]
    z = crossingover(best, best2)
#    print(best.money)
#    time.sleep(3)
    z1 = mutation(z[0])
    z2 = mutation(z[1])
    return z1, z2
for zz in range(0, gens):
    population = []
    for i in range(0, psize):   #population size
#    m = [[random.randint(0,1) for _ in range(13)] for _ in range(4)]
        m = [random.uniform(0,1) for _ in range(8)] 
        hand = []
        a = player(m, hand)
        population.append(a)
    fixation = [list(0 for _ in range(8)) for _ in range(20)] 
    for i in range(0,gens): #number of generations
#        print("Generation "+str(i))
        zzzz = i
        testfitness(population)
        newpop = []
        for j in range(0, int(len(population)/2)):
            z = tournament(population)
            grid1=z[0].grid[:] 
            hand = []
            hand2 = []
            b = player(grid1, hand)
            grid2 = z[1].grid[:]
            b2 = player(grid2, hand2)
            newpop.append(b)
            newpop.append(b2)
        if i%10==0:
            print("Currently at gen " + str(zz))
            for j in range(0,psize):
                #print(population[j].grid)
                #print(population[j].wins)
                for n in range(0,8):
                    if population[j].grid[n]==1:
                        fixation[int(i/10)][n]+=1
        zzz = 0
#    for i in range(0, len(population)):
#        print(population[i].grid)
#        print(population[i].money)
        population = newpop
    n = population[0].grid
    for i in range(1,psize):
        for j in range(0,8):
            n[j] += population[i].grid[j]
    for i in range(0,8):
        n[i] = n[i]/psize
    print(n)
valList = [0,0,0,0,0,0,0,0]
for i in range(0,psize):
    for j in range(0, 8):
        valList[j]+= population[i].grid[j]/psize
print(valList)
print("Grid values offer a possible superior selection of traits for optimal poker play based on calculation of odds, order, and behavior based on size of the pot.")