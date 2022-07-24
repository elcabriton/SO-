import threading
import time
 
from queue import Queue
from xml.dom.expatbuilder import theDOMImplementation




def euler(i,fila):

    e=1/fatorial(i)
    fila.put(e)
    # print(e)

def fatorial(n):
    resultado=1
    for i in range(1,n+1):
        resultado *= i
    return resultado





fila=Queue()

inicio=time.time()
threads=[]
x=int(input("quantas vezes quer repertir: "))
for i in range(0,x+1):
    # t=threading.Thread(target=euler,args=(x,fila))
    #if sum(fila.queue)<2.718281828459045:  
    t=threading.Thread(target=euler(i,fila))
    threads.append(t)
    t.start()
   # t.join()
    # else:
    #     print("ja era")
    #     break
    
for t in threads:
    t.join()
    
somatorio=sum(fila.queue)
print(somatorio)
fim=time.time()

