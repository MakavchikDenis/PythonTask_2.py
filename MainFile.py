
import random;
import datetime;
import prettytable;
import matplotlib.pyplot as plt;


array = [];
array_2=[];

def Sort(array): #пузырьковая сортировка №1
    for i in range(len(array)):
        for x in range(len(array)-1-i):
            if array[x]>array[x+1]:
                j=array[x];
                array[x]=array[x+1];
                array[x+1]=j;


def Sort_2(array_2): #сортировка select
    for i in range(len(array_2)):
        min=i;
        for j in range(i+1,len(array_2)):
            if array_2[j]<array_2[min]:
                min=j;
        var=array_2[min];
        array_2[min]=array_2[i];
        array_2[i]=var;



table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время select"])
x=[]
y1=[]
y2=[]

for i in range(1000,5000,1000):
    x.append(i);
    min =1;
    max=i;
    for j in range(i):
        array.append(random.randint(min,max));
    array_2 = array.copy();
    t1 = datetime.datetime.now();
    Sort(array);
    t2 = datetime.datetime.now();
    print(array);
    print("Пузырьковая сортировка заняла "+str((t2-t1).total_seconds())+ "c");
    y1.append(str((t2-t1).total_seconds()));
    t3=datetime.datetime.now();
    Sort_2(array_2);
    t4=datetime.datetime.now();
    print(array_2);
    print("Сортировка select заняла " +str((t4-t3).total_seconds())+"c");
    y2.append((t4-t3).total_seconds());
    table.add_row([str(i), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds())]);
    print("------------------");

print(table);
plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()











