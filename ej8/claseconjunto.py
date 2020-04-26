import csv

class conjunto:
    __conj=[]
    def __init__(self):
            self.__conj=[]
    def crearlista(self,lista):
        for i in range(len(lista)):
            lista[i]=int(lista[i])
        self.__conj=lista
    def mostrar(self):
        print(self.__conj)
    def __add__(self,x):
        self.__conj.sort()
        x.__conj.sort()
        listanueva=conjunto()
        for i in self.__conj:
            if i not in listanueva.__conj:
                listanueva.__conj.append(i)
        for i in x.__conj:
            if i not in listanueva.__conj:
                listanueva.__conj.append(i)
        return listanueva
    def __sub__(self,x):
        self.__conj.sort()
        x.__conj.sort()
        listanueva=conjunto()
        for i in self.__conj:
            if i not in listanueva.__conj:
                if i not in x.__conj:
                    listanueva.__conj.append(i)
        return listanueva
    def __eq__(self,x):
        self.__conj.sort()
        x.__conj.sort()
        l=False
        i=0
        if len(self.__conj)==len(x.__conj):
            while((i<len(self.__conj)) and (self.__conj[i]==x.__conj[i])):
                l=True
                i+=1
            if (l==True and i==len(self.__conj)):
                l=True
            else:
                l=False

        else:
            l=False
        return l
           




    
  
