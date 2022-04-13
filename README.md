# ejercicios-ordenar-buenos-

link:https://github.com/Javifdz12/ejercicios-ordenar-buenos-.git

1. Ordenación por inserción dicotómica
Sea t una tabla de una sola línea (vector) de elementos de un tipo T que derivan de COMPARABLE, y que hay que ordenar en orden creciente. Cada elemento está insertado en su lugar dentro del resultado que se ha de obtener buscando su posición de inserción mediante el algoritmo dicotomía estudiado en el capítulo «Iteración».

Las ordenaciones presentes en la sección anterior de este capítulo «Algunos algoritmos simples» no han usado la ayuda de una tabla adicional para construir el resultado. Modifican la tabla que hay que ordenar para reordenar sus componentes. Aquí estudiamos los dos tipos de soluciones haciendo intervenir el método de inserción por dicotomía.

Ejercicio 4: Ordenación por inserción dicotómica




Sea t una tabla de una sola línea donde los componentes son de tipo T images/flechedroite.png COMPARABLE.
- Escribir primero las especificaciones del algoritmo que no usa la ayuda de otra tabla para calcular su resultado.

Así, los elementos de t están «ordenados en su lugar». Cuidar especialmente la precondición y la postcondición; no son fáciles de obtener, pero proporcionan una guía útil para la construcción del algoritmo.

- Desarrollar el análisis completo de la solución retenida.

En la segunda estrategia de resolución, se define primero una tabla r inicialmente vacía con el mismo cardinal que t. Esta vez se inserta una copia de cada componente t «en su lugar» en r, buscando su posición, como en la primera estrategia que hemos visto antes.

- Desarrollar este algoritmo nuevo.

Este ejercicio es difícil, constituye un buen ejemplo de análisis/concepción guiada por las especificaciones. Por motivos de espacio y de legibilidad, las soluciones se estudian detalladamente en el archivo disponible para descargar desde la página Información.

2. Una ordenación topológica
Consideramos n tareas t1, t2… tn sometidas a las restricciones anteriores. Es decir, hay que terminar algunas tareas antes de poder empezar otras. Así, por ejemplo, primero tenemos que preparar los cimientos de una casa antes de montar las paredes y los tabiques. En el ejercicio siguiente se propone calcular una ordenación de tareas sometidas a restricciones de prioridad.

Ejercicio 5: Ordenación topológica





Una restricción se expresa mediante un par (i,j) de números enteros comprendidos entre 1 y n, que indica que la tarea ti va antes que la tarea tj. Es decir, la tarea ti debe estar terminada antes de empezar la tarea tj. La relación binaria «... precede ...» así definida en el conjunto de las n tareas es una relación de orden parcial: algunas tareas no son comparables.

Hacer un algoritmo que calcule una ordenación de la n tareas cumpliendo las restricciones.

Está claro que no se pueden cumplir todas las restricciones. En este caso, no hay ordenación de las tareas. El algoritmo deberá tratar este caso correctamente.

3. Completar las especificaciones
La sección «Algunos algoritmos simples» ha usado un predicado está_explorado que no se ha especificado completamente. En particular, hemos escrito: «cada componente de t[inicio .. fin] está colocado después de la serie más grande de componentes de la que es el max». El ejercicio siguiente propone completar esta especificación. Es un problema difícil.

Ejercicio 6: Especificación de está_explorado





Escribir las especificaciones del predicado está_explorado.

Las especificaciones se expresan usando la definición de un segmento de tabla. Es una serie de componentes que empieza por el máximo de la serie.

Definición

Se llama segmento en una tabla t de componentes de tipo T que deriva de COMPARABLE a la serie de componentes consecutivos más grande cuyo valor máximo es el primero de la serie.

La figura siguiente representa una tabla y sus segmentos.

images/08_07.png
La parte t[inicio .. fin] contiene dos segmentos. El primero en t[5 .. 9] tiene por componente máximo 18 en la celda t[5]. El segundo en t[10 .. 11] tiene por componente máximo 21 en t[10].

La tabla t[inicio .. fin] contiene k segmentos S1, S2, …, Sk. Cada segmento Si tiene un primer componente de número di y un último componente de número fi que verifican:

           (1 ≤ i ≤ k ) (Si = t[di .. fi]) 
            max 1 ≤ i ≤ k(Si) = t[di] 
            max 1 ≤ i ≤ k(Si) ≤ t[fi + 1] 
Para cada segmento Si, explorar consiste en:

Hacer copia de seguridad del max del segmento: mi images/flechegauche.PNG t[di];
Desplazar los elementos de t[di+1 .. fi] una celda hacia la izquierda;

Colocar el elemento más grande del segmento «en lo alto»: t[fi] images/flechegauche.PNG mi.
