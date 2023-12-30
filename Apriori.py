import pandas as pd

minSupp = 0.4;
minConf = 0.7; 

data   = pd.read_csv("supermarket.csv");
L = list();
Cur_L = list();
C = list();

cNum=1;

for cl in data:
    l = [cl];
    item = {'item':[cl],'count':(data[l] == 't').all(axis=1).sum() };
    C.append(item);

def newItem(listitem,count):
    newIt = {'item':listitem,'count':count };
    return newIt; 
#in ra table
def printTable(tb = [{'item':[],'count':1 }]): 
    print("===items",end='')
    # for i in range(0,len(tb[0]['item'])*4,1):
    #     print("=",end='');
    print("count===")
    for i in tb:
        print("",i['item'],"||",i['count']);
    print("========================");

def C_to_L():
    Cur_L.clear();
    for i in C:
        if i['count'] >= (minSupp*len(data)):
            Cur_L.append(i);
            L.append(i);
curlist = list()
def checkDouble(s):
    for i in curlist:
        if set(s) == set(i):
            return True;
    curlist.append(s);
    return False;

def compare(it1,it2):
    s = list(set(it1['item']+it2['item']) ); 
    #print(s)
    if(len(s) >cNum) or (len(s) < cNum) or checkDouble(s) :
        return 
    count  = (data[s] == 't').all(axis=1).sum()
    
    return newItem(s,count);        


def L_to_C():
    global cNum 
    cNum = cNum+1
    C.clear()
    for i in range(0 , len(Cur_L)-2 , 1):
        it1 = newItem(Cur_L[i]['item'],Cur_L[i]['count'])
        for j in range(i+1 , len(Cur_L) , 1):
            it2 = newItem( Cur_L[j]['item'] , Cur_L[j]['count'] )
            newitem = compare(it1,it2);
            if(newitem == None): 
                continue
            C.append(newitem)
    
def printL():
    print("============\ Day pho bien \================")
    print("L = {",end='')
    for i in L:
        print("    ",i['item'],": ",(i['count']/len(data))*100,"%")
    print("}")    
def Ariori() :

    while(True):
        printTable(C);
        C_to_L();
        
        printTable(Cur_L)
        L_to_C()
        if (C == []): 
            break


Ariori()
printL()
# print(L)



#_____________Luat ket hop____________________

Rules =list()
def newRule(left ,right,conf ):
    newr= {'left':left, 'right':right, 'conf':conf}
    return newr
def ConffOf(R,l):
    countL = sum((item['count'] for item in L if item['item'] == l) )
    countR = sum((item['count'] for item in L if item['item'] == R))
    # print(countL,countR)
    return countL / countR 

curR = list()



def powerset(items):
    result = []
    for i in range(2 ** len(items)):
        subset = [items[j] for j in range(len(items)) if (i & (1 << j)) > 0]
        result.append(subset)
    return result

def generate_associations(items):
    powerset_result = powerset(items)
    associations = []
    for subset in powerset_result:
        if subset:
            associations.append(subset)
    return associations

def calculatorRule(l):
    R = generate_associations(l)
    right = list();left = list();
    for i in R:
        if len(set(i)) == len(l):
            continue
        right = list(i)
        left = list(set(l)-set(right))
        if ConffOf(left,l) >=minConf:
            newr = newRule(left,right,ConffOf(left,l)*100)
            Rules.append(newr)
           


            

def printRules(R):
    i =0 
    for r in R:
        i = i+1
        print("\n R",i,r['left'],"-->",r["right"],": ",r['conf'],"%")
def AssociationRules(L):
    for l in L :
        if(len(l['item'])<=1):
            continue
        #print(l['item'])
        calculatorRule(l['item'])
        
AssociationRules(L)
printRules(Rules)
