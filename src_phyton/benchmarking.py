import random
import time
from metodos_ordenamiento import MetodosOrdenamiento
class Benchmarking:

    def __init__(self):
        print('Bench Inicializado')
    
    def ejemplo(self):
        self.mO = MetodosOrdenamiento()
        arreglo = self.buil_arreglo(50000)

        tarea = lambda: self.mO.sortByBubble(arreglo)

        tiempoMillis = self.contar_con_current_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)

        print(f'Tiempo en Milis: {tiempoMillis}')
        print(f'Tiempo en Nano: {tiempoNano}')

    def buil_arreglo(self, tamanio):
        array = []
        for i in range (tamanio):
            numero = random.randint(0, 99999)
            array.append(numero)
        return array
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()

        return (fin-inicio)

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()

        return (fin-inicio)/1000000000.0

    def medir_tiempo(self, tarea, arreglo):
        inicio = time.perf_counter()
        tarea(arreglo)
        fin = time.perf_counter()

        return fin-inicio