class MetodosOrdenamiento:

    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range (n):
            for j in range ( i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        
        return arreglo
    
    def sort_seleccion(self, arreglo):
        arreglo=arreglo.copy()
        n = len(arreglo)

        for i in range (n - 1):
            menor = i

            for j in range (i + 1, n):
                if arreglo[j] < arreglo[menor]:
                    mejor = j
            if mejor != i:
                arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

        return arreglo