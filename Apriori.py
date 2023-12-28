import pandas as pd

minSupp = 2;
minConf = 0.7; 

data   = pd.read_csv("sample.csv");
L = list();
Cur_L = list();
C = list();

cNum=1;

for cl in data:
    item = {'item':cl,'count':data[cl][data[cl] =='t'].count() };
    C.append(item);

def newItem(item,count):
    newIt = {'item':item,'count':count };
    return newIt; 
#in ra table
def printTable(tb): 
    print("===items========count===");
    for i in tb:
        print("   ",i['item'],"     ||   ",i['count']);
    print("========================");


def C_to_L():
    Cur_L.clear();
    for i in C:
        if i['count'] >= minSupp:
            Cur_L.append(i);
            L.append(i);
curlist = list()
def checkDouble(s):
    for i in curlist:
        if s == set(i):
            return True;
    curlist.append(s);
    return False;

def compare(it1,it2):
    global cur_item
    dem = 0;
    s = set(list(it1['item'])+list(it2['item'])); 
    if(len(s) >cNum) or (len(s) < cNum) or checkDouble(s) :
        return 
    for i in  range(0,len(data) ,1):
        #print(str(data.loc[i,[it1['item'],it2['item']]] == 't'))  
        if ( data.loc[i,[it for it in s] ]== 't').all() :
            dem = dem +1
            #print(dem)
    return newItem(''.join(s),dem);        


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
        print(i['item'],":",i['count'], end=" ; ")
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
        
# printTable(C);
# C_to_L();
# 
# printTable(Cur_L)
# L_to_C()
# 
# printTable(C);
# C_to_L();
# 
# printTable(Cur_L)
# L_to_C()
# 
# printTable(C);
# C_to_L();
# 
# printTable(Cur_L)
# L_to_C()
# 
# printTable(C);
# C_to_L();
# 
# printTable(Cur_L)
# L_to_C()