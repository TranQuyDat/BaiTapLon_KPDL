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

def compare(it1,it2):
    dem = 0;
    s = str(it1['item'])+str(it2['item'])
    for i in  range(0,len(data) ,1):
        #print(str(data.loc[i,[it1['item'],it2['item']]] == 't'))  
        if (data.loc[i,[it1['item'],it2['item']]] == 't').all():
            dem = dem +1
            #print(dem)
    
    return newItem(s,dem);        


def L_to_C():
    C.clear()
    for i in range(0 , len(Cur_L)-2 , 1):
        it1 = newItem(Cur_L[i]['item'],Cur_L[i]['count'])
        for j in range(i+1 , len(Cur_L)-1 , 1):
            it2 = newItem( Cur_L[j]['item'] , Cur_L[j]['count'] )
            newitem = compare(it1,it2);
            if(newitem == None): 
                continue
            C.append(newitem)
    

def Ariori:


printTable(C);
C_to_L();

printTable(Cur_L)
L_to_C()
printTable(C);
C_to_L();
printTable(Cur_L)