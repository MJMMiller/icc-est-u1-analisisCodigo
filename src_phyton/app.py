# import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Ben.Benchmarking()
    metodosOrden = MetodosOrdenamiento()
    benchmark = Benchmarking()

    tamanios = [500,1000,2000]
    resultados = []

    for tam in tamanios:
        arreglo_base = benchmark.buil_arreglo(tam)

        metodos = {
            "burbuja":metodosOrden.sortByBubble,
            "seleccion":metodosOrden.sort_seleccion,
        }
        
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)

        for resultado in resultados:
            tam, nombre, tiempo = resultado
            print (f"Tamano : {tam} || Metodo : {nombre} || Tiempo : {tiempo:.6f} segundos")

    tiempo_by_metodo = {
        "burbuja" : [],
        "seleccion" : []
    }

    #clasificar los tiempos segun el tiempo
    for tam, nombre, tiempo in resultados:
        tiempo_by_metodo[nombre].append(tiempo)
    
    #crear la grafica
    plt.figure(figsize=(10,6))


    for nombre, tiempo in tiempo_by_metodo.items():
        plt.plot(tamanios, tiempo, label= nombre, marker='o')

    #agregar parametros
    plt.grid()
    plt.suptitle('Comparativa metodos')
    plt.ylabel('Tiempos obtenidos')
    plt.xlabel('Tamaño del arreglo')
    plt.show()