#importación de bibliotecas
from time import sleep, perf_counter
from threading import Thread
#Instanciación del subproceso
def task(id):
    print(f"Iniciando tarea {id}\n")
    #responderá cada 2 segundos
    sleep(2)
    #es decir finalizará la tarea cada 2 segundos
    print(f"Finalizando tarea {id}\n")
    id*id*id*id

#retorna un valor despues de cierto tiempo 
start_time=perf_counter()

#coleccion de hilos
threads=[]
#ciclo para la asignación de cada hilo y su valor
for n in range(1, 2000):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
end_time=perf_counter()
print(f"Tomo {end_time- start_time:}")
