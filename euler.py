from multiprocessing import Pool, cpu_count
import sys  # para a recursiva
import time  # para calcular o tempo

def euler(i):
    e = 1/fatorial(i)
    return e
    # fila.put(e)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


sys.setrecursionlimit(1000000)
def main():
    #x = int(input("quantas vezes quer calcular: "))
    #y = int(input("quantas threads: "))
    x=10000
    y=2
    inicio = time.time()
   
    with Pool(y) as p:
        resultado=p.map(euler, range(0,x+1))
    somatorio=sum(resultado)
    print("Total: ",somatorio)
    
    fim = time.time()
    tempo = fim-inicio
    
    print ("utlizando pool: " + str(tempo) + 'resultado: ' + str(somatorio))
   

    vetor1=[]
    inicio1=time.time()
    for cont in range(0,x+1):
        vetor1.append(euler(cont))
   
    print("tempo sem thraeads: " + str(time.time()-inicio1) + "resultado: " + str(sum(vetor1)))
if __name__ == "__main__":
    main()