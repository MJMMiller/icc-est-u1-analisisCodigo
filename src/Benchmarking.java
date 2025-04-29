import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento mO;

    public  Benchmarking(){
        
        // long inicioMillis = System.currentTimeMillis(); //Fecha referencial ( epoch ) ms desde 1970 - 01 - 01 UTC
        // long inicioNano = System.nanoTime();

        // System.out.println(inicioMillis + " / " + inicioNano);

        mO = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);

        Runnable tarea = () -> mO.burbujaTradicional(arreglo); 

        double currentTime = medirConCurrentTime(tarea);
        double nanoTime = medirConNanoTime(tarea);

        System.out.println("Tiempo con Current Time: "+ currentTime);

        System.out.println("Tiempo con Nano Time: " + nanoTime );
    }

    private int[] generarArregloAleatorio(int tamaño){
        int[] arreglo  = new int[tamaño];
        Random random = new Random();
        for(int i = 0; i<tamaño; i ++){
            arreglo[i] = random.nextInt(1000_000);
        }
        return arreglo;
    }

    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin- inicio) / 1_000_000_000.0;
    }

    public double medirConCurrentTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin- inicio) / 1000.0;
    }
}