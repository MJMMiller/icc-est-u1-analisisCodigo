# import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":

    # Ben.Benchmarking()
    metodosOrden = MetodosOrdenamiento()
    benchmark = Benchmarking()

    tam = 10000
    arreglo_base = benchmark.buil_arreglo(tam)

    metodos = {"burbuja":metodosOrden.sortByBubble,
               "seleccion":metodosOrden.sort_seleccion,
    }
    
    resultados = []

    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaResultado = (tam, nombre, tiempo)
        resultados.append(tuplaResultado)

    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print (f"Tamano : {tam} || Metodo : {nombre} || Timpo : {tiempo:.6f} segunddos")