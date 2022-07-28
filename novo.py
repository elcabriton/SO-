
from multiprocessing import Pool
import sys  # para a recursiva
import time  # para calcular o tempo
import functools
from queue import Queue


def euler(i):
    e = 1/fatorial(i)
    return e


@functools.lru_cache(maxsize=10)
def fatorial(n):
    if n == 1:
        return n
    elif n <= 0:
        return 1
    else:
        return n*fatorial(n-1)


sys.setrecursionlimit(1000000)
if __name__ == '__main__':

    x = 90000
    y = 3
    vetor = [i for i in range(x)]
    fila = Queue()
    inicio = time.time()

    with Pool(processes=y) as p:

        resultado = p.map(euler, vetor)
        somatorio = sum(resultado)
        print("Total: ", somatorio)

    fim = time.time()
    tempo = fim-inicio

    print("utlizando pool: ", tempo)


vetor1 = []
inicio1 = time.time()
for cont in range(0, x+1):
    vetor1.append(euler(cont))

print("tempo sem threads: ", time.time()-inicio1)
