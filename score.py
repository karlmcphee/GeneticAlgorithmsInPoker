class score:

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
    
