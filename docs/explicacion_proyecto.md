# Proyecto explicado desde cero

## Cómo leer este documento

**1. Cada sección dice dónde mirar.** Al final de casi todas hay un bloque así:

    Dónde mirar. docs/part1/b1_phi_efficient_sets.md, sección 2.4. Busca las
    tres regiones en forma cerrada.

Sirve para una rastrear cualquier afirmación hasta el
fichero que la produjo.

**2. Cada sección lleva una etiqueta.** Una de estas tres:

    SLIDE   va a la presentación. Hay una diapositiva para esto.
    DECIR   merece decirse en voz alta, pero no ocupa diapositiva. Suele ser una
            frase de transición, una salvedad o una respuesta a una pregunta
            previsible.
    FONDO   es contexto escrito. Va en la memoria y en el registro. **Ponerlo en
            la presentación sería un error**: alarga, distrae y no aporta.

El objetivo es que la presentación se **recolecte** en lugar de escribirse desde
cero. La parte 13 lista las secciones SLIDE en el orden en que se cuentan, y esa
lista es el guion. La parte 13 apunta a unos quince minutos.

La etiqueta va en el título. Cuando una parte entera lleva una, vale para todo lo
que hay debajo; cuando la parte es sólo un contenedor — las partes 3, 5, 6, 7 y 8
— la etiqueta está en cada sección. Las secciones de servicio (ésta y el cierre)
no llevan etiqueta: no se presentan.

Una advertencia sobre las etiquetas FONDO: no significan "poco importante".
Varias de las cosas más sólidas del proyecto son FONDO, porque son garantías
sobre cómo se puede formular la afirmación y no resultados que se enseñen. Un
tribunal que pregunte por ellas se merece la respuesta; una diapositiva que las
lleve pierde el hilo.


## PARTE 1. El problema de fondo — SLIDE

### 1.1 Optimizar

Optimizar es buscar el mejor valor de algo. "Dame el punto donde el coste es
mínimo". Si sólo hay un objetivo (el coste), hay una respuesta: un punto.

### 1.2 Multiobjetivo

En la práctica casi nunca hay un solo objetivo. Quieres minimizar el coste **y**
minimizar el riesgo. Y normalmente se contradicen: bajar el coste sube el riesgo.

Analogía: optimizar un programa para que sea rápido y que gaste poca memoria. No
existe "el mejor programa". Existe un conjunto de compromisos.

Cuando hay varios objetivos ya no hay un ganador único. Hay un **conjunto** de
soluciones que no se pueden mejorar en un objetivo sin empeorar otro. A ese
conjunto se le llama **conjunto eficiente** (o frente de Pareto).

### 1.3 Dominancia

La regla que define ese conjunto se llama dominancia:

    La solución A domina a la solución B si A es igual o mejor que B en TODOS
    los objetivos, y estrictamente mejor en AL MENOS UNO.

Una solución es eficiente si nadie la domina. El conjunto eficiente es el
conjunto de todas las soluciones que nadie domina.

Esto es todo lo que hace falta saber de optimización multiobjetivo.

### 1.4 Incertidumbre: los intervalos

Hasta aquí hemos supuesto que sabemos los números exactos. En la realidad no.
El coste de algo no es "40". Es "entre 38 y 45", porque hay error de medida, o
porque el parámetro varía, o porque la información es incompleta.

Un **intervalo** es eso: `[38, 45]`. Un par de números que dice "el valor real
está aquí dentro, no sé dónde".

En optimización intervalar, cada objetivo devuelve un intervalo en lugar de un
número.

Dos palabras que se usan todo el rato y que conviene fijar ya, porque en la
memoria hay que distinguirlas y en español es fácil confundirlas:

    centro          el punto medio del intervalo, (38 + 45) / 2 = 41.5
    semianchura     la mitad de lo que mide, (45 - 38) / 2 = 3.5
    anchura         lo que mide entero, 45 - 38 = 7

**Semianchura y anchura no son la misma palabra y no se pueden intercambiar.**
El proyecto lo prohíbe expresamente porque dos de los tres órdenes se construyen
sobre una de las dos y confundirlas cambia el resultado.

    Dónde mirar. CONTEXT.md sección 4, la regla de vocabulario. Y
    src/interval_math.py, que es donde vive la aritmética de intervalos.


## PARTE 2. El problema central del proyecto — SLIDE

### 2.1 Los intervalos no se pueden ordenar

Con números reales siempre sabes cuál es menor: 3 < 7. Siempre.

Con intervalos, no. Coge `A = [1.5, 5]` y `B = [3, 7.5]`. ¿Cuál es menor?

- A empieza antes (1.5 < 3), así que en el mejor caso A es mejor.
- A también acaba antes (5 < 7.5), así que en el peor caso A también es mejor.
- Aquí A parece mejor. Pero coge `A = [1, 10]` y `B = [4, 5]`.
  A puede ser mejor (1 < 4) o mucho peor (10 > 5). No hay respuesta.

**Este es el problema central.** Y no es un problema técnico que se resuelva con
más esfuerzo: es que no existe una única forma correcta de ordenar intervalos.
Existen muchas, y cada una es una decisión sobre qué te importa.

Analogía de programación: tienes una lista de objetos con dos campos y quieres
ordenarla. No hay un orden natural. Tienes que dar una **función clave** (`key`
en Python). Y si cambias la función clave, cambia el resultado del `sort`.

### 2.2 Lo que hicieron tus tutores

Tus tutores (Beato Moreno y Osuna Gómez), en su artículo de 2024, hicieron algo
elegante: en vez de proponer *un* orden, describieron **toda la familia** de
órdenes posibles, con un parámetro que dice cuál estás usando.

Ese parámetro se llama **φ** (fi). Un φ es, en esencia, una función clave.

En el repositorio ese artículo es **[1]**, y está en `papers/` con su lista de
referencias completa.

### 2.3 Qué hace un φ, concretamente

Un φ coge un intervalo `[inferior, superior]` y devuelve **dos números reales**.
Una vez tienes dos números reales, ya sabes comparar, porque los reales sí se
ordenan.

Los tres φ que el artículo nombra son:

    φ de Ejemplo 2.2 (le llamamos "lu"):
        [inf, sup]  →  (inf, sup)
        No cambia nada. Compara el mejor caso con el mejor caso y el peor con el
        peor. Es el más conservador.

    φ de Ejemplo 2.3 (le llamamos "ls"):
        [inf, sup]  →  (inf, sup - inf)
        Devuelve el mejor caso y la anchura del intervalo, es decir, cuánta
        incertidumbre tiene.

    φ de Ejemplo 2.4 (le llamamos "cw"):
        [inf, sup]  →  ((inf+sup)/2, (sup-inf)/2)
        Devuelve el centro y la media anchura. Es decir: "el valor típico" y
        "cuánto puede variar".

Los tres son válidos. Los tres son distintos. Y cada uno da un conjunto eficiente
distinto.

Hay un cuarto ejemplo en el artículo, el Ejemplo 2.1, con otros coeficientes.
El proyecto no lo usa: no lleva asociada una noción de convexidad, que es lo que
hace falta para poder derivar nada a mano. Se anotó y se dejó.

    Dónde mirar. src/phi_transforms.py. Los tres φ salen de **una sola** función
    a la que le pasas cuatro coeficientes, y la condición de admisibilidad del
    artículo se comprueba dentro. Por eso añadir un cuarto φ es un bucle y no una
    reescritura. Y docs/part1/a0_framework.md, que es la lectura del artículo
    afirmación por afirmación, con página y número de ejemplo en cada una.

### 2.4 Por qué el problema se vuelve del doble de tamaño

Si tu problema tiene 2 objetivos intervalares, y cada intervalo se convierte en 2
números reales, entonces el problema transformado tiene **4 objetivos reales**.

Regla general: **m objetivos intervalares → 2m objetivos reales.**

Y esto es útil, porque un problema multiobjetivo real clásico ya se sabe
resolver: hay algoritmos hechos (NSGA-II, PSO).

El artículo demuestra que resolver el problema transformado es equivalente a
resolver el original.

Guárdate esto, porque tiene una factura que se paga en la sección 5.3: al pasar
de 2 a 4 objetivos, o de 3 a 6, la dominancia deja de discriminar. Con muchos
objetivos casi todo el mundo es no dominado por casi todo el mundo.

### 2.5 La pregunta de investigación

Ahora ya se puede formular lo que pidieron tus tutores:

    Si cambio φ y resuelvo el mismo problema, ¿cambian las soluciones que
    encuentro? ¿Cuánto? ¿Bajo qué condiciones?

**Hay una segunda pregunta que el proyecto no responde en ningún sitio: "¿qué φ
da mejores resultados?".** Cada φ manda el problema a un espacio distinto con una
escala distinta, así que comparar "calidad" entre φ es comparar peras con
manzanas. Sólo se podría responder con un criterio externo — por ejemplo el
rendimiento real de una cartera —, y ni los benchmarks ni los problemas
intervalares publicados traen criterio externo ninguno. El estudio de carteras es
trabajo futuro, que es donde la diapositiva 21 de los propios tutores lo pone.

Así que la pregunta del proyecto es una sola, y hay que decirla así:

    **cuánto cambia la respuesta cuando lo único que cambia es el orden.**

**Ningún documento del proyecto ordena los tres φ, y ninguna tabla los clasifica.**
Es una prohibición explícita y se comprueba al cerrar cada parte.

    Dónde mirar. CONTEXT.md sección 2, la prohibición. Y la sección 8 de
    docs/part1/part1_closing.md y la 9 de docs/part2/part2_closing.md, que son
    las dos comprobaciones de que no se ha incumplido.


## PARTE 3. Qué se ha hecho, en orden

El proyecto tiene fases. Te las cuento como lo que son: primero entender, luego
construir el problema, luego calcular la respuesta correcta a mano, luego
programar los algoritmos, luego comprobar que los algoritmos encuentran la
respuesta correcta, luego decidir con qué se mide, y por último medir.

**Las seis fases están hechas.**

### 3.1 Fase A — Entender el marco y construir los problemas

**A0: leer el artículo y verificar todo.** — DECIR

Se leyó el artículo afirmación por afirmación, anotando página y número de
ejemplo en cada una. De ahí salió también que existe un cuarto ejemplo, el 2.1,
con cuatro pares de coeficientes distintos y sin noción de convexidad asociada,
que es por lo que no se usa.

Regla del proyecto, y gobierna todo lo demás: **si algo no está verificado, no se
marca con un comentario y se deja; se quita.**

    Dónde mirar. docs/part1/a0_framework.md. Busca las filas v-01 a v-23: cada
    una es un hecho verificado con su ecuación o su número de ejemplo y su
    página. Todas las filas v-nn del proyecto viven en docs/verified.md.

**A1: cómo se mete la incertidumbre en un problema. Este es el hallazgo más
importante del proyecto.** — SLIDE

El plan original decía: coge un problema normal y súmale y réstale un ε
constante. Es decir, `f(x)` se convierte en `[f(x) - ε, f(x) + ε]`.

Parece razonable. Es fatal.

Piénsalo con la función clave. Si ε es constante, la anchura del intervalo es
siempre `2ε`, siempre la misma. Entonces:

    φ_lu  te da  (f - ε, f + ε)      → los dos números se mueven juntos con f
    φ_ls  te da  (f - ε, 2ε)         → el segundo número es CONSTANTE
    φ_cw  te da  (f, ε)              → el segundo número es CONSTANTE

Un campo constante no influye en una ordenación. Es como ordenar por
`(nombre, 7)`: el 7 no hace nada.

**Conclusión: con ε constante, los tres φ dan exactamente el mismo resultado, y
además el mismo que el problema sin incertidumbre.** El estudio habría medido
cero, no porque no haya efecto, sino porque el diseño lo hacía imposible.

Se comprobó midiendo, y el resultado es más fuerte que "el mismo tamaño": los
cuatro conjuntos (los tres φ y el problema sin incertidumbre) salieron con **los
mismos índices**, punto por punto, en ZDT1 con treinta variables y en DTLZ2 con
doce, sobre 5000 puntos.

Y no hace falta que la anchura sea constante para que pase. **Basta con que la
anchura sea una función exacta del centro.** Se midió con una imprecisión
proporcional, `f → [f(1-ε), f(1+ε)]`, donde la anchura varía muchísimo: los
cuatro conjuntos de índices volvieron a salir idénticos, con correlación +1.0000
entre centro y anchura. Por eso se descartó también meter la imprecisión en los
coeficientes: si un objetivo es un monomio en un coeficiente impreciso, su
semianchura es una función lineal exacta de su centro, y se cae en el mismo sitio.

La condición necesaria que sale de ahí, y que es la regla del proyecto: **la
anchura tiene que estar movida por una variable de decisión que el centro no
determine.**

Y salió un segundo hallazgo: en ZDT1 (un problema de referencia estándar), la
elección obvia de anchura también falla, porque la anchura se hace mínima justo
donde están las soluciones buenas. Pasa todos los tests estadísticos sobre una
muestra uniforme y aun así está mal. De ahí una tercera regla: comprobar que los
φ difieren sobre una muestra aleatoria del espacio **no es evidencia**, porque
una muestra aleatoria de una caja de treinta dimensiones casi no contiene puntos
cerca del conjunto eficiente. La comprobación se hace **donde vive el conjunto
eficiente**, no en la caja.

Las dos cosas están contadas con sus números en la parte 10.

    Dónde mirar. docs/part1/a1_uncertainty_model.md, partes 1 y 2. La parte 4
    lleva el barrido de niveles de imprecisión y la predicción, hecha antes de
    correr nada, de qué conjunto crecería y cuál no. El control negativo (la
    anchura proporcional que colapsa los tres órdenes) está asertado como test en
    tests/test_problems_tier1.py, o sea que si alguien lo rompe, salta.

**A2, A3: la aritmética y los órdenes.** — FONDO

Se programaron las operaciones con intervalos y los tres φ. Los tres φ se
construyen con una única función a la que le pasas los coeficientes, y se valida
contra la condición del artículo. Así, si mañana los tutores dicen que se puede
interpolar entre dos φ, es un bucle y no una reescritura.

**A3-b: un problema de precisión que habría corrompido todos los resultados.** — FONDO

Si calculas φ a partir de `[inferior, superior]`, la anchura te sale como
`(c + r) - (c - r)`, que en coma flotante **no** da exactamente `2r`. El error es
proporcional al tamaño del centro y cae entero en la columna de la anchura, que
es justo el segundo número de dos de los tres φ.

Medido: una anchura que de verdad toma 46 valores distintos salía con 210.

La solución no fue poner una tolerancia. φ es una función lineal, y pasar de
(centro, radio) a (inferior, superior) también, así que componer las dos da el
mismo φ evaluado en otro orden. El proyecto evalúa φ directamente sobre la
representación en la que el problema está realmente calculado. Las matemáticas no
cambian; sólo el orden de las operaciones.

Está contado entero, con las magnitudes, en la sección 10.3.

**A4, A5: los problemas.** — DECIR

- **p0**: el ejemplo que el propio artículo pone después de sus condiciones de
  optimalidad. Viene con respuesta publicada, así que sirve para comprobar que el
  procedimiento funciona antes de fiarse de él en otro sitio.
- **p1**: un problema de dos variables construido a propósito para que los tres φ
  den conjuntos distintos, no degenerados, y calculables a mano. Su caja es
  `[-0.5, 1.5]²`. Cada objetivo tiene su semianchura movida por la variable **del
  otro** objetivo, que es la regla de A1 aplicada.
- **ZDT1 y DTLZ2**: dos problemas de referencia estándar de la literatura,
  adaptados a intervalos. ZDT1 con treinta variables, DTLZ2 con doce.

Una palabra que hace falta más adelante: p1, ZDT1 y DTLZ2 son problemas
**adaptados**. Eran problemas normales y el proyecto les puso una banda de
incertidumbre encima. Eso es exactamente lo que la parte 2 existe para responder.

    Dónde mirar. src/problems_tier0.py (p0 y p1) y src/problems_tier1.py (ZDT1 y
    DTLZ2 intervalares). En problems_tier0.py, busca `p1_default_params`: el
    comentario de encima explica por qué ρ = 1/4 y no otro valor, y no es cuestión
    de gusto sino de que el conjunto eficiente quede dentro de la caja.

### 3.2 Fase B — Calcular la respuesta correcta a mano — SLIDE

Aquí está la parte que a tus tutores les va a interesar más.

**B1: derivar el conjunto eficiente en forma cerrada.**

"Forma cerrada" significa: una fórmula exacta, deducida con papel y lápiz, no un
resultado aproximado de un ordenador.

Usando el Teorema 3.3 y el Ejemplo 3.9 del artículo de tus tutores — es decir,
sus propios resultados, aplicados, no reinventados — se dedujo exactamente cuál
es el conjunto eficiente de p1 bajo cada uno de los tres φ.

Sale bien porque p1 está construido para que todo sea cuadrático, y entonces la
condición de optimalidad se convierte en un sistema lineal que se resuelve
explícitamente. Sin búsqueda de raíces en ningún sitio.

Los tres resultados son la imagen que tienes, y están explicados en la parte 4.

**Por qué esto es lo que hace que todo lo demás sea posible, y es la frase que
hay que decir en voz alta:** sin una respuesta exacta no puedes preguntarte
"¿cuánto se equivoca mi instrumento?". Con ella sí, y ese número existe y está en
la sección 3.6.

**Y se verificó en las dos direcciones**, en aritmética racional exacta, sin coma
flotante: 12341 vectores de pesos hacia delante, ninguno cayendo fuera de la
región que la fórmula dice; y 301 puntos de la región hacia atrás, ninguno sin su
peso testigo. Es decir: la fórmula no se queda corta ni se pasa.

También se dice honestamente lo que **no** se cerró: en dos direcciones
particulares de pesos las condiciones publicadas dan sólo optimalidad débil y no
dicen si esos puntos son óptimos o no. No se parcheó. Extender una condición
publicada es trabajo de tus tutores, no tuyo. **Y se puso precio a no saberlo**:
con la muestra de la región fija y el segmento añadido encima, una métrica de
calidad se mueve entre −0,63 % y +5,36 %, que es suficiente para dar la vuelta a
una comparación ajustada. Es la pregunta s-12 y sigue abierta.

**B2: meter esa fórmula en código**, para poder comparar contra ella. La función
que devuelve el conjunto de referencia **no tiene valor por defecto** para el
interruptor de los segmentos singulares: quien la llama tiene que decir cuál de
las dos versiones quiere, y ese valor va en cada tabla. Es la forma de que una
decisión no resuelta no se cuele como si estuviera resuelta.

    Dónde mirar. docs/part1/b1_phi_efficient_sets.md, sección 2.4 para las tres
    fórmulas y sección 2.6 para lo que no cerró. El código es
    src/reference_fronts.py; busca `include_singular_segments`.

### 3.3 Fase C — Los algoritmos y la comprobación — DECIR

**C1: búsqueda aleatoria.** No es un competidor, es el **control** del
experimento. Es el único método cuyo muestreo no depende de φ, así que puedes
coger *una* muestra y filtrarla con los tres φ: entonces las tres respuestas
difieren *sólo* por el orden. En NSGA-II y PSO, φ dirige también la búsqueda, y
los dos efectos se mezclan. Esto se explica entero en la sección 3.5 porque es el
diseño del experimento y no un detalle de implementación.

**C2: NSGA-II y MOPSO**, de la librería pymoo, sin modificar.

**C3: la puerta de validación.** ¿Los algoritmos encuentran lo que B1 dedujo?

Noventa medidas: tres algoritmos × tres φ × cinco semillas × dos ajustes del
interruptor de los segmentos singulares. Se asertan **dos direcciones**:

    ¿encuentran lo que existe?       la distancia desde el conjunto deducido
                                     hasta lo que devuelve el solver
    ¿encuentran algo mejor?          cuántos puntos del conjunto deducido son
                                     dominados por un punto del solver

La segunda es la que habría acusado a la derivación: si un solver encontrase algo
mejor que la fórmula, la fórmula está mal. **Cero en las noventa.** La derivación,
su codificación y los tres algoritmos están de acuerdo sobre dónde está el
conjunto eficiente.

La primera falla en **doce de noventa**, y todas son NSGA-II: tres semillas bajo
φ_ls y tres bajo φ_cw, en los dos ajustes del interruptor. Los márgenes son
pequeños, de 0.005 a 0.039 en una caja de lado 2.

Eso son los "12 tests que fallan". **No son un fallo del proyecto: son un
resultado.** NSGA-II reparte sus 100 puntos por el conjunto eficiente peor que
un muestreo uniforme del mismo conjunto con los mismos 100 puntos, bajo dos de
los tres φ y no bajo el tercero. Su distancia de relleno cae en el percentil 85 a
99 de mil sorteos uniformes bajo los dos φ donde ocurre, y en el 33 a 60 bajo el
tercero, que es donde cae un sorteo uniforme.

Están marcados en el código como fallo esperado **estricto**, de forma que si
apareciera un decimotercero, o si uno de los doce dejara de fallar, salta el
aviso. **La aserción sigue corriendo sobre las noventa**; lo que está fijado es
qué doce fallan. La suite tiene 1074 tests: 1062 pasan y 12 fallan a propósito.

**La mitad del efecto tiene explicación y la otra mitad no, y hay que decirlo
así.** La mitad se explica porque la búsqueda aleatoria — que no depende de φ
para nada — arrastra la misma diferencia: +0.243 de un total de +0.483 al pasar
de φ_lu a φ_ls. Es la forma de las regiones actuando sobre el comparador, no
NSGA-II. La otra mitad es de NSGA-II y **se descartaron cinco explicaciones
midiéndolas una por una**. Ninguna sirve. **No sabemos por qué**, y así está
escrito en el entregable.

Una consecuencia que sí es importante y va en la sección 3.5: **por eso el
resultado principal se mide sobre búsqueda aleatoria y no sobre NSGA-II.**

    Dónde mirar. docs/part1/c3_validation.md, sección 5 para el hallazgo y
    sección 4.1 para la decisión de no eximir a NSGA-II de la aserción. El código
    de la puerta es tests/test_validation.py; los doce xfail estrictos están
    ahí, con los nombres de las semillas.

### 3.4 Fase D — Las métricas, y por qué hay dos familias — SLIDE

Esta sección es corta de leer y es **la idea más importante de todos los
resultados**. Si en la presentación sólo entra una diapositiva conceptual, es
ésta.

**El problema.** Quieres decir "cambiar de φ cambia la respuesta, y cambia
*esto*". Para eso hace falta un número. ¿Qué número?

**Hay dos sitios donde medir, y no valen para lo mismo.**

**Familia 1: métricas en el espacio de objetivos.** Hipervolumen, IGD, spread.
Se calculan sobre lo que devuelve el solver: las 2m columnas de la imagen.

Sirven para comparar **algoritmos con un φ fijo**. "¿NSGA-II lo hace mejor que
MOPSO bajo el Ejemplo 2.4?" — eso sí.

**No sirven para comparar φ entre sí, y la razón es la clave de todo.** Cada φ
manda el problema a un espacio distinto. Un hipervolumen es el volumen de una
región; bajo φ_lu esa región vive en un espacio y bajo φ_cw en otro, con otros
ejes y otra escala. Dividir uno entre otro no significa nada, igual que dividir
kilómetros entre kilogramos.

Analogía de programación: es como comparar el tamaño en bytes de dos ficheros
comprimidos con dos algoritmos distintos y concluir cuál tiene "mejor
contenido". Los bytes no son del mismo tipo.

**Familia 2: métricas en el espacio de decisión.** Cobertura, distancia de
Hausdorff, solapamiento.

Se calculan sobre las **variables de decisión**, no sobre los objetivos. Y el
espacio de decisión es **el mismo para todos los φ**: es la caja donde vive `x`,
y cambiar de orden no la cambia. Un punto `x = (0.3, 0.9)` es el mismo punto bajo
los tres φ.

**Aquí sí se pueden comparar. Y aquí vive el resultado del proyecto.**

Otra forma de decirlo, que es la que va en voz alta: la pregunta no es "¿qué
frente sale más bonito?", es "**¿qué decisiones te quedan encima de la mesa?**".
Y una decisión es un `x`, no un valor de objetivo.

#### Qué mide cada una, en palabras

Las tres se calculan entre **dos conjuntos de puntos** — el conjunto que sale con
un φ y el que sale con otro.

    cobertura(A → B)   qué fracción de A ya está en B.
                       Es ASIMÉTRICA: cobertura(A→B) y cobertura(B→A) son dos
                       números distintos y hay que dar los dos.
                       "Si yo trabajo con el orden A y tú con el B, ¿qué parte de
                       mis soluciones ya tenías tú?"

    Jaccard            qué fracción de la UNIÓN comparten.
                       |A ∩ B| / |A ∪ B|. Un número solo, simétrico.
                       1 = idénticos, 0 = sin nada en común.

    Hausdorff          la mayor distancia que hay que recorrer.
                       Para cada punto de A, la distancia al punto más cercano de
                       B; te quedas con la peor. Y al revés. Y con la peor de las
                       dos.
                       Es un MÁXIMO, así que lo decide un solo punto: el peor
                       colocado.

Hay una cuarta que aparece en los ficheros y conviene reconocerla: el
**coeficiente de Dice**, `2|A∩B| / (|A|+|B|)`. Es otra convención del mismo
solapamiento, no otra cosa. Se convierte en Jaccard con
`jaccard = dice / (2 - dice)`, y el proyecto usa esa identidad y la escribe cada
vez que la usa. **La función `compute_overlap` del código devuelve Dice, no
Jaccard**, y esto ha sido fuente de confusión suficiente como para decirlo aquí.

#### Un ejemplo pequeño, inventado

Esto **no es un dato del proyecto**; es para ver las definiciones funcionando.
Dos conjuntos de tres puntos en el plano:

    A = { (0,0), (1,0), (2,0) }
    B = { (0,0), (1,0), (5,5) }

Comparten dos puntos. Entonces:

    cobertura(A → B) = 2/3 = 0.667     dos de los tres puntos de A están en B
    cobertura(B → A) = 2/3 = 0.667     dos de los tres puntos de B están en A
    Jaccard          = 2/4 = 0.500     comparten 2 de los 4 puntos distintos
    Dice             = 4/6 = 0.667     y 0.667 / (2 - 0.667) = 0.500, cuadra

    Hausdorff:
        de A a B: el punto (2,0) tiene su más cercano en (1,0), a distancia 1
        de B a A: el punto (5,5) tiene su más cercano en (2,0), a distancia 5.83
        simétrica: 5.83

**Y aquí se ve para qué sirve cada una.** Cobertura y Jaccard dicen lo mismo:
"comparten dos tercios / la mitad". **Ninguna de las dos ve que el punto que
sobra en B está lejísimos.** Hausdorff sí lo ve, y no ve nada más: le da igual
que el resto coincida.

Por eso el proyecto **da siempre las dos coberturas antes que el solapamiento**,
y nombra la convención del solapamiento cada vez. Un solo número nunca describe
la relación entre dos conjuntos.

#### Delta: el parámetro que hay que declarar

"¿Está el punto de A en B?" necesita una tolerancia: dos números en coma flotante
casi nunca son idénticos. Ese margen se llama **delta** y se da como fracción del
diámetro de la caja.

**Delta no tiene valor por defecto en el código.** A propósito: dos coberturas
con dos deltas son dos cantidades distintas y no se comparan entre sí, así que
quien llama tiene que decir cuál quiere y el valor va en cada tabla.

**Y el resultado es que delta cero es el único valor legible del proyecto.** Con
delta cero, además, no es un límite ni una aproximación: los tres conjuntos de
una comparación son **conjuntos de índices sobre un mismo array**, así que dos
vectores de decisión o son el mismo punto bit a bit o son dos puntos, y la
cobertura es un recuento exacto sin ninguna tolerancia dentro.

Cualquier delta positivo es una decisión de ajuste presentada como una medida. Se
comprobó tres veces, y las tres por causas distintas: en p1 la cobertura casi se
duplica y se satura dentro del rango barrido; en los benchmarks la misma fracción
es un instrumento distinto en cada dimensión, porque las distancias crecen con la
raíz del número de variables; y en I-BK1 el problema es de escala, con una caja
de `[-10,10]²` y los conjuntos viviendo en `[0,5]²`.

    Dónde mirar. src/metrics_decision.py, cuya cabecera es la explicación de por
    qué esta familia y no la otra; y src/metrics_objective.py, cuya cabecera dice
    qué hace pymoo distinto de la definición del libro y no lo esconde. El
    barrido de delta está en results/tier0/delta_sweep.csv y
    results/part2/delta_sweep.csv.

### 3.5 Fase E — El diseño del experimento: una muestra, tres filtros — SLIDE

Esta es la parte más ingeniosa del diseño y la más fácil de explicar. Si hay una
diapositiva sobre método, es ésta.

**El problema que resuelve.** Quieres saber cuánto cambia la respuesta al cambiar
el orden. Pero si corres NSGA-II tres veces, una con cada φ, has cambiado **dos
cosas a la vez**:

    1. el criterio con el que se decide quién es no dominado   ← lo que quieres medir
    2. la búsqueda misma, porque NSGA-II usa φ para elegir a quién cruza y a
       quién mata, así que con otro φ visita otras zonas del espacio   ← ruido

Los dos efectos salen mezclados y no se pueden separar. Una diferencia medida
sobre salidas de NSGA-II está **confundida** con el comportamiento de NSGA-II
bajo cada orden.

**La solución.** La búsqueda aleatoria no mira los objetivos para decidir dónde
mirar: sortea puntos en la caja y ya está. Su muestra es una función pura de la
caja, del presupuesto y de la semilla. **No depende de φ.**

Así que:

    1. sorteas UNA muestra de 5000 puntos
    2. evalúas el problema UNA vez sobre esos puntos
    3. filtras esa misma evaluación TRES veces, una con cada φ

Y entonces los tres conjuntos que salen **difieren sólo por el orden**. No hay
otra explicación posible: la muestra es la misma, la evaluación es la misma, los
índices apuntan al mismo array.

Analogía: es un experimento con un control perfecto. Mismo paciente, mismo día,
tres diagnósticos con tres criterios. Lo que cambia es el criterio.

**Y de aquí sale la frase que hay que decir en voz alta**, porque es
contraintuitiva y porque contesta a la pregunta que va a hacer alguien:

    La búsqueda aleatoria no es el rival flojo del experimento. Es el
    instrumento que lleva el resultado principal. NSGA-II y MOPSO están para
    otra cosa: para comprobar que la derivación es correcta y para medir lo que
    le cuesta a un algoritmo de verdad.

Esto no es una racionalización posterior. La propia diapositiva 17 de la
propuesta de los tutores pide la búsqueda aleatoria como *referencia base*, y lo
que el proyecto descubrió es que esa referencia base es la única con la propiedad
de aislamiento que hace falta.

    Dónde mirar. src/random_search.py, la función
    `filter_one_sample_under_every_phi`. Son cinco líneas y el comentario de
    encima dice exactamente esto. Y src/metrics_decision.py, función
    `compare_phi_on_one_sample`, cuyo comentario explica por qué esta y no las
    tiradas de los solvers.

**Qué se corrió, exactamente.** — DECIR

    e1, tier 0     p0 y p1. Tres solvers × tres φ × cinco semillas (11 a 15) ×
                   dos presupuestos. 36 configuraciones, 180 tiradas.
    e2, tier 1     ZDT1 con 30 variables y DTLZ2 con 12. Lo mismo, más un barrido
                   de cinco niveles de imprecisión (ε = 0, 0.05, 0.10, 0.25,
                   0.50). 108 configuraciones, 540 tiradas.
    f3, parte 2    I-BK1, el problema publicado. Lo mismo. 18 configuraciones,
                   90 tiradas, 741.93 segundos.

El presupuesto es **5000 evaluaciones** (población 100 × 50 generaciones), con
una comprobación de convergencia a **20000**, que es la rejilla entera repetida.
Cinco semillas por configuración, para poder dar una mediana y un recorrido en
lugar de un número suelto.

**Y una regla que conviene mencionar porque es lo que hace el trabajo
auditable:** los registros de las tiradas (`e1_tier0_run.md`,
`e2_tier1_results.md`, `f3_native_run.md`) están **generados**. Cada número que
llevan se lee de vuelta de un fichero que la tirada escribió. Volver a correr el
script tiene que reproducirlos exactamente. **Ningún número de un registro está
tecleado a mano.**

### 3.6 Fase E — Los números — SLIDE

Cuatro cosas, en este orden. Las cuatro son de la parte 1.

#### 3.6.1 p1 exacto contra p1 medido: el error del instrumento

Este es el corazón del proyecto y es la razón de que exista p1.

En p1 sabemos la respuesta exacta (fase B). Y también podemos **medirla** con el
instrumento (la muestra filtrada tres veces). Poner las dos al lado da una cosa
que casi ningún trabajo empírico tiene: **cuánto se equivoca el instrumento.**

Sobre el par de cabecera, φ_lu contra φ_cw, a presupuesto 5000:

    cantidad                     exacto      medido      error relativo
    cobertura(lu → cw)           0.394710    0.555932    +40.8 %
    cobertura(cw → lu)           0.122571    0.221859    +81.0 %
    Jaccard                      0.103177    0.187190    factor 1.81

A presupuesto 20000 los tres errores bajan: +27.7 %, +48.6 %, y el factor del
Jaccard pasa de 1.81 a 1.49.

**Léelo así, que es lo que significa.** El instrumento dice que los dos órdenes
comparten el 18.7 % cuando de verdad comparten el 10.3 %. **Se equivoca hacia
arriba: exagera el acuerdo.** Todas las filas van en la misma dirección y todas
se encogen al cuadruplicar el presupuesto.

Y la razón de que se equivoque hacia arriba es intuitiva: con una muestra finita
encuentras un puñado de puntos de cada conjunto, y los puntos que encuentras
tienden a ser los fáciles, que son los que están en la parte compartida. Lo que
sólo pertenece a un conjunto está en los bordes y se muestrea peor.

    Dónde mirar. results/tier0/instrument_error_p1.csv. **Es el único fichero del
    proyecto que pone una cantidad deducida al lado de la misma cantidad medida**,
    hasta que la parte 2 produjo el segundo. Los valores exactos vienen de
    results/tier0/exact_regions_p1.csv y los medidos de
    results/tier0/table_2_measured.csv, bloque de decisión, delta 0.0.

#### 3.6.2 Los números de los benchmarks, y por qué son cotas y no estimaciones

En ZDT1 (30 variables) y DTLZ2 (12) no hay fórmula cerrada: no se puede saber la
respuesta exacta. Sólo se puede medir. Los números, sobre la misma muestra
filtrada tres veces, a delta cero y presupuesto 5000:

    problema  n    ε      cob(lu→cw)  cob(cw→lu)  Jaccard   |X_lu|  |X_cw|
    zdt1      30   0.00   1.000000    1.000000    1.000000     18      18
    zdt1      30   0.05   0.846154    0.088000    0.086614     26     257
    zdt1      30   0.10   0.722222    0.101167    0.094891     36     257
    zdt1      30   0.25   0.660000    0.120623    0.108772     53     257
    zdt1      30   0.50   0.545455    0.159533    0.133117     68     257
    dtlz2     12   0.00   1.000000    1.000000    1.000000    150     150
    dtlz2     12   0.05   0.897541    0.138267    0.136486    278    1813
    dtlz2     12   0.10   0.851964    0.167527    0.162312    351    1813
    dtlz2     12   0.25   0.779967    0.245375    0.229867    575    1813
    dtlz2     12   0.50   0.684211    0.371760    0.321871    980    1813

Fíjate en la primera fila de cada bloque: con ε = 0 no hay incertidumbre, todo
vale 1, los tres órdenes coinciden. **Es la comprobación de cordura**: cuando no
hay intervalos, el orden no puede importar.

**Y ahora la frase que hace que estos números valgan.** Como el mismo
instrumento, en el mismo problema y al mismo presupuesto, mide un acuerdo 1.81
veces mayor del real, **cada acuerdo medido es una cota superior**. Los órdenes
comparten **menos** de lo que dicen las tablas.

Es decir: no son estimaciones que puedan estar de más o de menos. **Son cotas
inferiores de la diferencia**, y eso es más fuerte que una estimación, porque un
crítico no puede decir "estos números están inflados a tu favor" — están
inflados en tu contra.

**Dos salvedades que no se pueden dejar caer.** La primera: **el signo del sesgo
se midió que se transfiere; la magnitud no**. Que el instrumento exagere hacia
arriba se comprobó en los benchmarks por la vía indirecta de cuadruplicar el
presupuesto y ver que las nueve estadísticas se mueven en la misma dirección,
nueve de nueve. Pero **el factor 1.81 es de p1 y no se aplica a ningún número de
benchmark en ninguna parte**. Decir "el Jaccard verdadero de ZDT1 es 0.087 / 1.81"
está prohibido explícitamente.

La segunda es de la parte 2 y corrige a la parte 1: en I-BK1 la respuesta al
presupuesto **no** es uniforme (cinco filas de nueve se acercan al valor exacto,
dos se alejan y dos no se mueven). Así que la frase "todas las filas se encogen
al subir el presupuesto", cierta en p1, **no es una propiedad general del
instrumento**. Lo que sobrevive es el signo medido directamente contra una
respuesta conocida, en los dos problemas donde se conoce.

    Dónde mirar. results/tier1/table_2_measured_eps_*.csv, bloque de decisión,
    delta 0.0. Los Jaccard salen de results/tier1/overlap_conventions.csv por la
    identidad con Dice. Y results/tier1/inherited_instrument_error.csv, que es la
    columna de error de p1 que e2 lee de vuelta para llevarla al lado de sus
    propias medidas.

#### 3.6.3 La dependencia de ε: cuál conjunto se mueve y cuál no

Mira otra vez las dos últimas columnas de la tabla. Ahí está la explicación
entera de la dependencia con ε, y es más limpia de lo que parece.

    |X_cw|   257 en ZDT1 y 1813 en DTLZ2, en TODOS los niveles positivos
    |X_lu|   26 → 36 → 53 → 68 en ZDT1, y 278 → 351 → 575 → 980 en DTLZ2

**El conjunto de φ_cw no se mueve. El de φ_lu crece. Toda la dependencia con ε es
de φ_lu.**

**Y que φ_cw no se mueva no es casualidad ni un artefacto: es demostrable.** El
argumento cabe en tres líneas y se puede decir en voz alta:

    bajo φ_cw la imagen es (centro_1, semianchura_1, ..., centro_m, semianchura_m)
    ε entra sólo multiplicando las semianchuras por una constante positiva
    multiplicar una columna por una constante positiva no cambia quién domina a
        quién, porque es una reetiquetación estrictamente creciente de esa columna

Así que el conjunto no dominado bajo φ_cw de una muestra dada **es el mismo
conjunto de índices para cualquier ε > 0**. La columna de cardinalidades lo
confirma exactamente en los cuatro niveles positivos.

**Y la dirección estaba predicha antes de correr nada**: en
`docs/part1/a1_uncertainty_model.md`, parte 4, escrito cuando se colocaron los
cinco niveles, dice que φ_lu es el sensible y φ_cw el estable. Se confirmó.

**Lo que no estaba predicho en ningún sitio** es que la cobertura y el Jaccard se
muevan en direcciones opuestas: la cobertura de X_lu en X_cw **baja** con ε
mientras el Jaccard **sube**. No están en conflicto; es aritmética de la
invariancia de arriba, y salió al escribir la síntesis.

La frase honesta, que es la que hay que llevar:

    Al crecer la imprecisión, el conjunto eficiente de φ_lu crece hacia dentro y
    hacia fuera del de φ_cw, que está fijo. La fracción de la respuesta de φ_lu
    que φ_cw rechazaría sube del 15 % al 45 % en ZDT1 y del 10 % al 32 % en DTLZ2.

    Dónde mirar. docs/part1/e3_synthesis.md, sección 3.1, para el argumento de la
    invariancia. La predicción registrada está en
    docs/part1/a1_uncertainty_model.md parte 4, y su cierre en la fila r-22 de
    PROGRESS.md sección 7.

#### 3.6.4 El número de la presentación: del 63 al 91 %

De todos los números del proyecto, éste es el que va en la diapositiva:

    **Entre el 63 y el 91 % del conjunto eficiente de un orden queda fuera del
    del otro, en todos los niveles de imprecisión, en los dos benchmarks.**

Concretamente entre 0.628240 y 0.912000 en las ocho celdas, con un recorrido
entre semillas del 1 al 4 % de esa cifra.

**Qué número es exactamente.** Es `1 − cobertura(cw → lu)`: la fracción del
conjunto de φ_cw (Ejemplo 2.4) que queda fuera del conjunto de φ_lu (Ejemplo
2.2). Dicho en decisiones: **si trabajabas con el Ejemplo 2.4 y te pasas al 2.2,
entre el 63 y el 91 % de lo que tenías sobre la mesa deja de estar disponible.**

**Y ahora lo importante: por qué esa dirección y no la contraria.** Porque es la
que aguanta.

La otra dirección — la fracción de X_lu que queda fuera de X_cw — también se mide
y también se mueve, y de hecho baja monótonamente de 0.846 a 0.545 en ZDT1. **Pero
cuatro de sus ocho celdas no pasan el criterio de estabilidad entre semillas**, y
todas las que fallan son celdas cuya mediana está pegada a 1.0 sobre un X_lu
pequeño — 26, 36 y 53 puntos en ZDT1. La que peor falla, ZDT1 con ε = 0.05, tiene
un recorrido entre semillas tan ancho como su distancia entera a 1.0.

La dirección que se presenta pasa el criterio en **las ocho celdas**, con ratios
de 0.007 a 0.037.

Dicho sin tecnicismos: **con cinco semillas distintas, el número de la
presentación se mueve poco y el otro se mueve mucho.** Así que se presenta el que
se mueve poco, y **se dice que el otro se midió y que no se puede citar como
cifra**. La pérdida se declara, no se absorbe.

Y hay una cosa que hay que decir aunque incomode, porque un tribunal la va a
notar: **la forma del desacuerdo no es la misma en p1 que en los benchmarks.** En
p1 los dos conjuntos se cruzan de verdad — cada uno tiene una zona a la que el
otro no llega. En los benchmarks X_lu está casi entero dentro de un X_cw mucho
más grande. La columna del Jaccard sola diría que las dos situaciones son
parecidas. No lo son, y la lectura para quien decide es distinta.

    Dónde mirar. docs/part1/part1_closing.md, sección 3.1, que es de donde salen
    las ocho celdas y el criterio de estabilidad. Los datos crudos están en
    results/tier1/table_2_measured_eps_*.csv, columnas median e iqr.


## PARTE 4. La imagen, explicada — SLIDE

Los dos ejes son las dos variables de decisión de p1. El rectángulo fino exterior
es la caja donde se puede buscar, `[-0.5, 1.5]²`.

**Lo que ves NO es un resultado de un algoritmo.** Son las tres fórmulas exactas
deducidas en B1, dibujadas. Es matemática, no experimento. No hay muestreo, no
hay semilla y no hay solver dentro de esta imagen.

- **La línea de puntos** es el conjunto eficiente con φ_cw (Ejemplo 2.4, centro y
  media anchura): exactamente el cuadrado unidad. Área 1.
- **La línea discontinua** es el conjunto con φ_ls (Ejemplo 2.3): el cuadrado
  [0, 4/3]² recortado por un arco. Área 1.513401. Es el más grande.
- **La línea continua** es el conjunto con φ_lu (Ejemplo 2.2, el conservador):
  una lente entre dos arcos. Área 0.310533. Es cinco veces más pequeño que el
  otro.

**Los tres puntos marcados** — (0, 4/5), (4/3, 1), (0, 4/3) — no son decoración.
Salen de la derivación: son donde las curvas se cortan y donde están los óptimos
de cada coordenada. Que caigan exactamente ahí es la comprobación de que la
fórmula es correcta.

**Los dos hechos que hay que señalar:**

1. La lente y el cuadrado de puntos están **los dos dentro** de la región
   discontinua. Eso no es casualidad de este problema: se sigue de un criterio
   conocido aplicado a los coeficientes de los tres ejemplos, y vale para
   **cualquier** problema del marco de tus tutores. Está en la sección 5.1.

2. La lente y el cuadrado **no se contienen el uno al otro**. La lente sube por
   encima de x₂ = 1, donde el cuadrado no llega; el cuadrado cubre todo lo de
   abajo, donde la lente no llega. **Cada uno tiene una zona que el otro no puede
   alcanzar.**

El segundo hecho es el que hace que exista un resultado. Si un conjunto estuviera
dentro del otro, una de las dos direcciones de cualquier estadístico estaría
fijada de antemano y no habría nada que medir. **Por eso el par de cabecera del
proyecto es Ejemplo 2.2 contra Ejemplo 2.4 y no un promedio sobre los tres pares.**

Y aquí van las tres cifras exactas, con sus direcciones:

    Los conjuntos de Ejemplo 2.2 y Ejemplo 2.4 comparten el 10.3 % de su unión.
    El 39.5 % del de 2.2 está dentro del de 2.4, y el 12.3 % del de 2.4 está
    dentro del de 2.2.

Leído al revés, que es como se presenta:

    **El 60.5 % del conjunto de 2.2 queda fuera del de 2.4, y el 87.7 % del de
    2.4 queda fuera del de 2.2.**

La cifra que va a la presentación es el 87.7 %, por la razón que explica la
sección 3.6.4: es la dirección estable.

En medida de Lebesgue exacta, sin muestreo y sin ningún solver dentro. **La
elección de φ no es un detalle, es la mitad del problema.**

    Dónde mirar. La figura es results/meeting/derived_regions_p1.png. Los números
    salen de results/tier0/exact_regions_p1.csv: claves coverage_a_in_b,
    coverage_b_in_a, overlap_union_share y area, sobre el par (lu, cw). Y las
    fórmulas de las tres regiones están en docs/part1/b1_phi_efficient_sets.md
    sección 2.4.


## PARTE 5. Los tres hallazgos que son sobre el marco de tus tutores

Estos no son sobre el código. Son sobre su artículo, y son lo que más les puede
interesar. **Los tres están fuera de la presentación**, y eso es una decisión
tomada a propósito: son garantías sobre cómo se puede formular la afirmación, no
resultados que se enseñan. Si los preguntan, se contestan.

### 5.1 La contención — DECIR

Hay un criterio conocido en optimización multiobjetivo: si transformas los
objetivos con una matriz de entradas no negativas e invertible, la relación de
dominancia se conserva. Aplicándolo a las matrices de coeficientes de sus propios
Ejemplos 2.2, 2.3 y 2.4 sale que:

    conjunto eficiente de 2.2  ⊂  conjunto eficiente de 2.3
    conjunto eficiente de 2.4  ⊂  conjunto eficiente de 2.3
    2.2 y 2.4 no se contienen mutuamente

De los seis mapas posibles entre los tres φ, **exactamente dos** cumplen la
condición, y los dos salen de 2.3. Ninguno de los dos mapas entre 2.2 y 2.4 es no
negativo, así que **nada relaciona a esos dos** y por eso son el par informativo.

Consecuencia práctica: **la comparación informativa es 2.2 contra 2.4**. Comparar
cualquiera de los dos con 2.3 es medir en parte un teorema. Y se ve en las
tiradas: esas dos coberturas salen 1.000000 con recorrido entre semillas
0.000000, en todos los niveles, en los dos benchmarks, en los dos presupuestos y
también en p1.

**Y aquí está la disciplina que conviene enseñar si preguntan.** La contención
**no se usa para afirmar nada**. Se usa sólo para **retirar** dos de los tres
pares de la evidencia, que es la dirección conservadora. Si los tutores refutan
el criterio, se quita la instrucción, se reportan los tres pares igual, y **el
número de cabecera no se mueve**, porque nunca salió de esos pares.

Su artículo tiene un resultado equivalente (Proposición 5.1) pero sólo para el
caso difuso, no para el intervalar. Se buscó el análogo intervalar
exhaustivamente y no está.

**Hay una comprobación independiente del criterio en la literatura.** La
Proposición 4.2 de Ishibuchi y Tanaka (1990), página 223, demuestra para un
**cuarto** orden la contención que el criterio predice. **Eso es una comprobación del criterio, no una respuesta a la
pregunta.** La pregunta sigue siendo s-11 y tiene tres partes: ¿es correcto el
criterio?, ¿son correctas las dos contenciones?, y ¿está publicado en algún
sitio? La tercera es la que decide si la memoria cita un resultado conocido o
anota una observación propia.

    Dónde mirar. docs/part1/a_close_containment.md, secciones 1 y 2 para el
    criterio y 6 para lo que se le pregunta a los tutores. La comprobación de
    Ishibuchi y Tanaka está en docs/part2/lit_review.md sección 2.4. En el código,
    src/metrics_decision.py, el diccionario `containments` y la función
    `pair_note`: cada par que involucra a φ_ls sale de las tablas etiquetado como
    "comprobación" y no como "hallazgo", y la etiqueta viaja con el número.

### 5.2 Las relaciones exactas entre los tres φ — FONDO

Las imágenes de los tres φ son transformaciones lineales fijas unas de otras, y
las matrices **no contienen ningún parámetro del problema**. Es decir, valen para
cualquier problema del marco. Los números de condición salen exactos: **1** entre
2.2 y 2.4 — o sea que son la misma figura girada y escalada — y exactamente el
número áureo al cuadrado, **2.618034**, para la que involucra a 2.3. Comprobado
con error 0.000e+00 sobre 500 puntos aleatorios de la caja.

**Por qué esto está en el documento y fuera de la presentación:** es una garantía
negativa. Como pointwise los mapas de 2.2 y 2.4 son el mismo salvo una semejanza,
**ninguna frase del tipo "el mapa de 2.2 distorsiona más que el de 2.4" puede ser
cierta**, y cualquier medida que parezca mostrarlo está midiendo la región sobre
la que se promedió. Es un guardarraíl sobre cómo se puede hablar del resultado.

Lo que **no** dice: nada sobre los conjuntos solución. La dominancia no se
conserva por un mapa lineal invertible cualquiera, sólo por uno de entradas no
negativas, que es el criterio distinto de la sección 5.1. Las dos matrices de
aquí tienen entradas negativas.

    Dónde mirar. docs/part1/c3_validation.md, sección 5.5. Ahí están las dos
    matrices escritas y los tres números de condición.

### 5.3 El coste de transformar — DECIR

Al pasar de m objetivos a 2m, incluso un problema de dos objetivos se vuelve un
problema de "muchos objetivos", donde la dominancia deja de discriminar: casi
todo el mundo es no dominado por casi todo el mundo, y el algoritmo se queda sin
criterio para elegir.

**Medido en los benchmarks, y el resultado está ordenado:**

    las 24 configuraciones de NSGA-II con imprecisión positiva — los dos
    benchmarks, los tres φ, los cuatro niveles — saturan el rango 1 en todas las
    semillas. Las tres únicas que no lo hacen son el caso sin incertidumbre.

    y la generación en que ocurre, de 50: en DTLZ2, la 2 en todos los niveles
    bajo 2.3 y 2.4, y 6, 4, 3, 2 bajo 2.2. En ZDT1, la 5 bajo 2.4, la 4-3 bajo
    2.3, y **23, 17, 15, 13 bajo 2.2**.

**φ_lu (Ejemplo 2.2) es el que aguanta más tiempo con presión de dominancia, en
los dos solvers y en los dos problemas, y lo que aguanta baja monótonamente al
subir la imprecisión.**

Qué significa para leer esos frentes: desde la generación en que satura, la
dominancia no selecciona nada y **la distancia de apiñamiento lo selecciona
todo**. O sea que el frente es un resultado de **reparto**, no de
**convergencia**. Y a nivel de benchmarks no hay ninguna medida de convergencia:
no existe frente de referencia para ZDT1 ni DTLZ2 transformados, así que el IGD
no está definido allí.

Esto es exactamente la crítica que Cui et al. (2024) — el artículo [7] — hacen a
los métodos basados en transformación, y aquí sale con números propios en lugar
de como cita. **No dice que ningún solver esté mal configurado**: dice lo que le
hacen 2m objetivos a cualquier selección basada en dominancia.

    Dónde mirar. results/tier1/rank_one_summary.csv, que sale de un callback de
    pymoo que deja el frente idéntico bit a bit. Y docs/part1/part1_closing.md
    sección 4.3.


## PARTE 6. Qué se predijo, y qué salió

Lo que hace que estas respuestas valgan es que las predicciones estaban
**escritas y fechadas antes** de la medida, así que no se pueden reinterpretar a
posteriori. Dos de ellas salieron mal, y las dos están aquí.

### 6.1 Las cuatro expectativas generales — DECIR

**"Los conjuntos cambian mucho al cambiar φ."** — **Confirmado, y con dos tipos
de evidencia.** Exacto en p1: comparten el 10.3 % de su unión, en medida de
Lebesgue. Medido en los benchmarks: del 63 al 91 % de un conjunto fuera del otro.

**"La diferencia crece con el nivel de incertidumbre."** — **Ni confirmado ni
refutado: la pregunta estaba mal planteada, y ésa es la respuesta.** Depende de
qué estadístico mires, y **dos de ellos se mueven en direcciones contrarias**: la
cobertura baja (la diferencia crece) mientras el Jaccard sube (el solapamiento
crece). Los dos son ciertos a la vez, y la sección 3.6.3 explica por qué. Lo que
sí se predijo bien, y estaba escrito con nombre y apellidos antes de correr, es
**cuál de los dos conjuntos es el sensible**: φ_lu crece con ε y φ_cw está fijo.

**"La búsqueda aleatoria da señal limpia y NSGA-II una más sucia."** —
**Confirmado**, y es el hallazgo de la sección 3.3: NSGA-II cubre el conjunto
eficiente peor que un muestreo uniforme al mismo número de puntos, bajo dos de
los tres φ. Es la razón de que el resultado principal se mida sobre búsqueda
aleatoria.

**"En DTLZ2 los algoritmos irán flojos por tener 6 objetivos; la búsqueda
aleatoria debería aguantar."** — **Confirmado.** En DTLZ2 NSGA-II satura la
dominancia en la **generación 2** de 50 en todos los niveles bajo dos de los tres
φ. La búsqueda aleatoria no depende de presión selectiva y no le afecta.

### 6.2 Las cuatro predicciones registradas formalmente — FONDO

Estas son distintas de las anteriores: se registraron en `PROGRESS.md` con sus
umbrales fijados **antes** de la tirada, en el sentido en que se registra una
hipótesis para que no se pueda ajustar después.

**x-01, la condición del minimizador protegido. Confirmada en DTLZ2 y no
comprobable en ZDT1.**

La idea: si una columna de la imagen es función de sólo algunas de las variables,
el punto que la minimiza está protegido — nadie puede dominarlo — y **sus otras
coordenadas quedan libres**, o sea que puede estar en cualquier sitio y aun así
salir en el frente. Se predijo antes de correr que el efecto aparecería
exactamente donde hay columnas así.

Confirmado en DTLZ2, y por una comparación más fuerte de la que pedía: **columna
contra columna dentro de un mismo φ**, que es lo que elimina cualquier
explicación basada en que el orden sea distinto. La columna con pocas variables
libres mide exactamente 0.000000, y las de once variables libres miden de 0.737 a
0.843.

**Y va con una prohibición que hay que respetar.** El cero exacto de esa columna
es un hecho sobre **la estructura de DTLZ2**, no sobre el Ejemplo 2.2. La frase
"φ_cw tiene minimizadores protegidos y φ_lu no" **no se puede escribir**. La
condición es una propiedad de una columna, y los órdenes sólo entran en la medida
en que determinan qué columnas existen.

En ZDT1 la predicción quedó **no comprobable**, no refutada: se registró contra
una versión del problema que después cambió, y sobre la versión que se corrió la
condición dice "presente" bajo los tres φ, así que ZDT1 nunca podría haber
discriminado.

**x-02. Sigue abierta, y es la medida más barata del proyecto.** Pedía veinte
semillas de búsqueda aleatoria sobre p1 bajo el Ejemplo 2.4. La tirada e2 sólo
hizo tier 1, así que no hay fila de p1 y ningún artefacto la decide. La lectura
con cinco semillas da 0.163 ± 0.094 contra un 0.125 predicho: **no es una
confirmación**, porque dentro de ese margen cabe el 0.125 y también el cero. Es
el mismo código que e1 ya corrió; nadie lo ha corrido con veinte semillas.

**m-1. Falló, y el fallo es un resultado.** Era un instrumento registrado con sus
dos umbrales fijados de antemano. Medido: dio 8.22 donde la predicción decía "a
lo sumo 1.5", y de 1.65 a 2.27 donde decía "al menos 3". Es decir, **no
discrimina, y se ve desde los dos lados a la vez**. El mecanismo que quería medir
sigue en pie (es x-01, confirmado arriba); el instrumento no. **Se retiró: no se
reajustaron los umbrales y no se reinterpretó.** Y que los umbrales estuvieran
fijados de antemano es justamente lo que hizo visible el fallo.

**m-2. Confirmada** en la misma tirada.

### 6.3 Un control que se construyó y no sirvió — FONDO

El plan tenía un control propio: un **suelo de ruido**, la diferencia entre dos
tiradas del mismo φ con dos semillas distintas. La idea era "cualquier diferencia
entre dos φ menor que esto es ruido".

Se construyó, se corrió, se barrió y **no tiene punto de operación**. A delta
cero da exactamente cero en cualquier dimensión, porque dos muestras uniformes
independientes no comparten ningún punto. Y a delta positivo es una función
escalón que depende de la dimensión: con la misma fracción del diámetro de la
caja, en DTLZ2 da de 0.73 a 0.95 y en ZDT1 da exactamente 0.000000.

**Se retiró tal como estaba medido** y se sustituyó por el recorrido entre
semillas del propio estadístico, calculado sobre una muestra filtrada tres veces
— que es su variabilidad de muestreo completa. **El sustituto es más débil que un
suelo de ruido y la memoria lo dice.**

    Dónde mirar. PROGRESS.md sección 9, que es donde viven las predicciones
    registradas con su redacción original. results/tier1/noise_floor_sweep.csv
    para el suelo de ruido. results/tier1/overhang_summary.csv para x-01 y
    results/tier0/registered_measurements_summary.csv para x-02.


## PARTE 7. Lo que está fijado, y lo que sigue abierto

### 7.1 Lo que está fijado — DECIR

**1. La parte 1 es un test controlado sobre problemas adaptados.** Su propósito
era hacer los órdenes comparables entre sí, y lo consiguió. Por eso la parte 1 se
**presenta** como un test controlado y no se **defiende** como si fuera realista.

**2. Se pueden buscar más φ, sujeto a las condiciones del marco.** La condición
de admisibilidad del artículo es sólo "determinante no nulo", así que interpolar
entre el Ejemplo 2.2 y el 2.4 da automorfismos admisibles **por la propia
definición del artículo**, sin necesidad de permiso. **No se ha hecho** — es la
curva de sensibilidad, y es lo primero que se recortó por calendario.

**3. La parte 2 son los problemas intervalares de origen** de un artículo
publicado, sin añadirles incertidumbre nosotros. El estudio de carteras es
trabajo futuro, que es donde la propia diapositiva 21 de los tutores lo pone. Es
lo que da lugar a toda la parte 8 de este documento.

**4. El corpus está abierto.** Todos los artículos están en `papers/` y no hay
exclusiones a nivel de artículo. Eso hace contestables varias preguntas de
lectura y cerró la única cifra sin verificar que quedaba en la derivación de la
fase B.

**5. Los entregables son tres**, para el 25 de septiembre: la presentación, que
es el entregable de verdad; una memoria informal de lo que se ha hecho; y un
artículo si da tiempo.

### 7.2 Lo que sigue abierto — FONDO

**Nueve preguntas siguen abiertas y todas merecen hacerse.** No hay ninguna que
bloquee trabajo: cada una lleva escrita la hipótesis sobre la que el proyecto
avanza mientras tanto.

Las dos que cambiarían algo:

    s-11   la contención. Tres partes: ¿es correcto el criterio?, ¿son correctas
           las dos contenciones?, ¿está publicado? La tercera decide si la memoria
           cita o si observa. **El número de cabecera no depende de ninguna.**
    s-12   los dos segmentos singulares donde las condiciones publicadas no dan
           veredicto. **Es la única pregunta que cambia un número** de los
           resultados finales, y el coste de no saberlo está medido: de −0.63 % a
           +5.36 % en una métrica de calidad.

Las siete de lectura, que cambian lo que se puede afirmar pero no lo que se ha
medido: s-01 (los subíndices de una ecuación), s-02 (si un "peso ≥ 0 no todos
nulos" hay que leerlo como estrictamente positivo — el proyecto tiene **dos
testigos** en contra de la lectura estricta, uno de p1 y otro de I-BK1), s-03,
s-04, s-06, s-07 y s-09 (dos decisiones de diseño que quieren visto bueno) y s-10.

Y tres tareas de lectura del propio proyecto que el corpus abierto hizo
contestables y que nadie ha hecho: p-01, p-04 y p-06.

    Dónde mirar. docs/plan_after_meeting.md es el plan de trabajo. El texto
    entero de cada pregunta abierta está en docs/supervisor_questions.md, escrito
    para poder contestarse de una sentada. Las cerradas están en docs/answered.md
    con el razonamiento que las retiró.


## PARTE 8. La parte 2: los problemas intervalares de origen

### 8.1 Por qué hacen falta problemas intervalares de origen — SLIDE

Aquí hay que ser honesto, porque es la crítica más obvia al proyecto y hay que
adelantarse a ella.

**p1, ZDT1 y DTLZ2 son problemas adaptados.** Eran problemas normales, sin
incertidumbre, y el proyecto les puso una banda de intervalos encima. Y no una
banda cualquiera: una banda **diseñada para que los tres órdenes no coincidan**,
porque la fase A había descubierto que la banda obvia los hace coincidir.

Un crítico puede decir, con toda la razón del mundo:

    "Habéis construido un problema para que dé la respuesta que queréis que dé.
    Si hubieseis puesto una banda constante, os habría salido cero, y lo sabéis
    porque lo medisteis."

**Y es verdad.** El proyecto lo mide y lo escribe: bajo la anchura lineal
rechazada, dos de los tres órdenes dan conjuntos idénticos y el tercero da el
orden sin incertidumbre.

Y ése es exactamente el punto: **el sujeto de verdad es la incertidumbre
genuina**, no una banda que nos hemos inventado.

**"Intervalar de origen" significa: los intervalos son del propio problema.** Los
coeficientes están publicados como intervalos por otros autores, para otro
propósito, antes de que este proyecto existiera. Nosotros no elegimos nada sobre
ellos: ni el ancho, ni qué variable lo mueve, ni si los órdenes van a separarse o
no.

Y por eso responde a la objeción: **si sobre un problema que no hemos construido
los tres órdenes vuelven a dar tres conjuntos distintos, el efecto no es un
artefacto del diseño.**

### 8.2 La puerta: cinco criterios escritos antes de mirar — DECIR

Hay una trampa evidente en "busca un problema publicado que sirva": si eliges el
criterio después de mirar los problemas, eliges el problema que te conviene.

Así que los cinco criterios se escribieron **antes de ver ningún ejemplo**, en
el plan de trabajo. Un problema sirve sólo si cumple **los cinco**; el que cumple
cuatro se reporta con el que falló y no se usa.

    1. dimensión      lo bastante pequeño para poder comparar los conjuntos en el
                      espacio de decisión con nuestro presupuesto.
    2. forma cerrada  ¿se puede deducir el conjunto eficiente a mano, y con qué
                      resultado publicado, nombrado por teorema o ejemplo?
    3. separación     los tres φ tienen que dar conjuntos distintos, ninguno igual
                      al problema sin incertidumbre y ninguno la caja entera —
                      **comprobado donde vive el conjunto eficiente y nunca sobre
                      una muestra uniforme de la caja**. Este criterio es la
                      lección de la fase A convertida en regla de admisión.
    4. la anchura     ¿alguna columna de la imagen depende sólo de algunas
                      variables? No descalifica: es la condición x-01 y un problema
                      que la tenga sirve de tercer test del mecanismo.
    5. de origen      **los intervalos son del propio artículo.** Un ejemplo cuyo
                      objetivo sea f(x) ± una constante, o ± una función que el
                      artículo se inventó para que fuera intervalar, **falla**,
                      porque eso es lo que ya hizo la parte 1.

**Qué pasó al aplicarlos.** Se leyó el artículo [16] — Mondal, Ghosh y Kim,
*Newton Method for Multiobjective Optimization Problems of Interval-Valued Maps*,
arXiv, marzo de 2026 — y se transcribieron **los veinte problemas** de su
apéndice A, uno por bloque, con sus dimensiones, su caja y sus objetivos en la
notación del propio artículo.

    criterio 5:  pasan 19 de 20. Los problemas son coeficientes intervalares del
                 propio artículo. **El único que falla es I-CH**, que es
                 f(x) ± 1 — es decir, **la degeneración de anchura constante de
                 la parte 1, apareciendo en un problema publicado**.
    criterio 3:  **no se puede contestar leyendo**, porque hace falta una muestra
                 cerca del conjunto eficiente y el artículo no la da. Y "no
                 determinable" no es un aprobado.
    resultado:   **ningún ejemplo pasa la puerta sólo con la lectura, y ninguno la
                 suspende.** Cinco pasan todos los criterios que una lectura puede
                 decidir: I-BK1, I-SD, I-IKK1, I-VFM1 y I-MHHM2.

El criterio 3 no se contesta con un diagnóstico muestreado, sino **derivando**.
Si eres capaz de deducir los tres conjuntos en forma cerrada, sabes si son
distintos **en medida de Lebesgue**, que es mucho mejor evidencia que cualquier
muestra.

    Dónde mirar. docs/part2/lit_review.md. Sección 1.8 lleva la tabla de los
    veinte problemas y la sección 1.9 el veredicto criterio por criterio. Los
    cinco criterios originales están en docs/part1/part1_closing.md sección 7.2,
    escritos antes de que se abriera el artículo, que es lo que hay que poder
    enseñar si alguien pregunta.

### 8.3 I-BK1: qué es el problema — SLIDE

Es el problema 1 del apéndice A de [16], en su página 27:

    G_1 = [0.1, 0.2] ⊙ x_1²  ⊕  [0.1, 0.3] ⊙ x_2²
    G_2 = [0.1, 0.3] ⊙ (x_1 − 5)²  ⊕  [0.1, 0.5] ⊙ (x_2 − 5)²
    con x en la caja [−10, 10]²

Léelo en voz alta y verás lo que importa: **los corchetes están en los
coeficientes.** No hay ninguna función de anchura escrita por nosotros. `[0.1,
0.2]` significa "este coeficiente vale algo entre 0.1 y 0.2 y no sabemos qué". Es
un problema de dos variables, dos objetivos, y por lo tanto cuatro columnas
reales al transformarlo.

**Y hay una comprobación que hace falta para poder decir que el efecto no es
nuestro.** La degeneración de la fase A ocurre cuando centro y semianchura son
proporcionales. Si en este problema lo fueran, los tres órdenes coincidirían y no
habría nada. Se comprobó, en racionales exactos: los cocientes son 1/3 contra 1/2
en el primer objetivo y 1/2 contra 2/3 en el segundo. **No son proporcionales**, y
**ninguno de los cinco problemas candidatos lo es**. Esa independencia es de
[16], no nuestra.

Un detalle técnico que hay que mencionar y no explicar: como todos los términos
son cuadrados, el producto de Moore no intercambia las funciones frontera, así
que las cuatro funciones frontera son las obvias. Es la condición que el propio
[16] enuncia para que la lectura en 2m columnas sea válida. **Se cita esa
condición en lugar de defender la construcción por nuestra cuenta**, y viene de
un artículo que no está defendiéndola tampoco.

### 8.4 La derivación: tres cuñas — SLIDE

El resultado de derivar I-BK1 a mano es más bonito de lo esperado, y se puede
contar entero.

**Toda la respuesta es un solo número.** Definiendo

    ν  =  x_2 (5 − x_1)  /  ( x_1 (5 − x_2) )

resulta que cada conjunto eficiente es exactamente **el conjunto de puntos cuyo ν
cae en un intervalo cerrado**. Y el intervalo depende del φ:

    φ_cw  (Ejemplo 2.4)    ν en [3/4, 3/2]      área 2.875612
    φ_lu  (Ejemplo 2.2)    ν en [2/3, 5/3]      área 3.790332
    φ_ls  (Ejemplo 2.3)    ν en [1/2, 2]        área 5.685282

Geométricamente, cada uno es una **cuña** entre dos hipérbolas que van de (0,0) a
(5,5); las tres están clavadas en esas dos esquinas. Por eso la comparación de
tres regiones del plano se convierte en la comparación de tres intervalos en una
recta.

**Y aquí está el resultado que hay que decir, y la salvedad que va pegada a él.**

Los seis extremos se ordenan estrictamente:

    1/2  <  2/3  <  3/4  <  3/2  <  5/3  <  2

Es decir: **los tres conjuntos están anidados**. `X_cw` dentro de `X_lu` dentro
de `X_ls`, las tres inclusiones estrictas.

**En p1 dos de los tres se cruzaban. Aquí los tres se anidan.** Y eso significa
que **la cantidad de cabecera de la parte 1 no tiene equivalente aquí**: la
pregunta "¿qué fracción de cada conjunto queda fuera del otro, sin que ninguno
contenga al otro?" no se puede plantear en I-BK1, porque una dirección de cada
par vale exactamente 1.

Lo que sí se puede decir, y es exacto, sin muestreo y sin ningún solver dentro:

    **el 49.4 % del conjunto mayor queda fuera del menor**, y los tres tamaños
    son 2.88, 3.79 y 5.69 sobre la misma caja.

**Por qué se anidan: hay mecanismo, y no es una demostración.** Sabemos por qué
el desacuerdo es unidimensional — todo se reduce a ν, porque las doce
coordenadas de la imagen (las cuatro columnas de cada uno de los tres φ) son
cuadráticas diagonales con coeficientes estrictamente positivos, y porque no hay
ninguna dirección singular de pesos bajo ningún φ, donde en p1 había dos bajo dos
de los tres φ. Pero eso **no fuerza el anidamiento**:
dos intervalos pueden solaparse parcialmente, y dos conjuntos así se cruzarían
igual que los de p1. **El anidamiento es una propiedad numérica de los
coeficientes impresos en [16]**, que resulta que ordenan estrictamente.

Así que la frase honesta es:

    **es una observación con un mecanismo localizado, no un resultado.** La frase
    "los órdenes se anidan en los problemas intervalares de origen" **no se puede
    escribir**: un problema de cada tipo no establece eso. Lo que sí se puede
    decir es que las dos geometrías son distintas, que la diferencia está
    localizada en la estructura de los coeficientes, y que se puede comprobar en
    cualquier problema nuevo antes de correrlo.

**Y hay un problema concreto que lo decidiría.** I-IKK1, el problema 11 del mismo
apéndice, es intervalar de origen **y tiene la estructura de p1** en lugar de la
de I-BK1: sus semianchuras dependen de una sola variable cada una. Si sus tres
conjuntos se cruzan, la diferencia entre las dos geometrías está en la estructura
de la anchura y no en la procedencia del problema. Si se anidan, es la primera
evidencia de lo contrario. **Los dos resultados valen la pena**, que es lo que no
pasa con otro problema de la forma de I-BK1. Cuesta dos sesiones y no cabe antes
del 25 de septiembre. **Está registrado como lo más valioso que la parte 2 no
hizo.**

### 8.5 La segunda medida del instrumento, y el resultado que da — DECIR

La parte 1 dijo qué haría falta para pasar de "una medida calibrada" a "un
instrumento calibrado": un segundo problema con respuesta conocida. I-BK1 es ese
segundo punto, y el resultado es concreto y algo decepcionante, que es como
suelen ser los resultados reales.

**El signo se transfiere.** De las nueve filas, seis miden por encima del valor
exacto, dos caen justo encima (y son las dos contenciones, fijadas de antemano) y
una por debajo. La que cae por debajo es la única dirección que ninguna
contención cubre. Es decir: **en cada fila libre de moverse, el instrumento
declara más acuerdo del que hay**, igual que en p1.

**La magnitud no se transfiere, y ése es el hallazgo.** El factor de p1 era 1.81.
En I-BK1 los tres pares dan 1.2517, 1.0067 y 1.4828. **Se diferencian casi en el
doble entre pares del mismo problema.** O sea: **1.81 es una propiedad de la
geometría de p1**, y ningún factor se transporta a ningún sitio. Lo que un lector
puede llevarse de estos cuatro números es el signo y nada más.

**Y todas las magnitudes de I-BK1 caben dentro de las de p1.** El mayor error
relativo es +48.3 % contra el +81.0 % de p1. La regla de parada del encargo — que
un error mayor que el de p1 acusaría a la codificación o a la derivación — no
saltó, y no se ajustó nada para que cuadrara.

**Y hay una comprobación externa, la primera del proyecto, y pasa.** El artículo
[16] publica en su ecuación (25) una curva de un parámetro. Calculada, esa curva
tiene ν = 162/169 = 0.958580 **constante a lo largo de toda su longitud**, y ese
valor cae estrictamente dentro de las tres cuñas. Además, ocho de los once puntos
que el artículo tabula la reproducen a seis decimales y otros dos son sus
esquinas. **Hasta aquí, todas las derivaciones del proyecto descansaban en su
propia álgebra. Ésta la confirma un tercero.**

    Dónde mirar. docs/part2/f2_ibk1_derivation.md para la derivación (sección 2.4
    las tres cuñas, sección 3.1 el anidamiento, sección 4.1 la comprobación
    externa que pasa). docs/part2/f3_native_run.md para la tirada.
    results/part2/exact_regions_ibk1.csv lleva los valores exactos y
    results/part2/instrument_error_ibk1.csv la segunda medida del error. Las 24
    figuras están en results/part2/figures/: los paneles de espacio de decisión a
    presupuesto 5000 son donde se ve el anidamiento, y son el compañero natural
    de las figuras de p1, donde se ve el cruce.


## PARTE 9. El contraejemplo — SLIDE

**Esto es lo más consecuente que encontró el proyecto**, y esta parte está
escrita para que puedas defenderla si te preguntan. El orden es deliberado:
primero los hechos que cualquiera puede comprobar, luego el mecanismo, y al final
los límites de lo que se afirma.

Y hay que enmarcarlo bien desde el principio: **es una corrección, no una
crítica.** El proyecto leyó ese artículo con lupa porque sus problemas son los
únicos problemas intervalares de origen que tenía disponibles. Todo lo que sigue
salió de tomarse en serio las definiciones y los números impresos del propio
artículo.

### 9.1 Qué afirma el artículo

[16] publica en su Tabla 1, página 20, el punto que su algoritmo devuelve tras
doce iteraciones en su primer problema de prueba (que es I-BK1, el de la parte
8):

    x⋆ = (3.914930, 1.428474)

y en la página 21 lo llama **punto Pareto óptimo** de ese problema.

Su propia definición 2.17 dice qué significa eso: que no existe otro punto
factible `x` con `G_i(x) ⪯ G_i(x⋆)` en los dos objetivos. Y su definición 2.2 dice
qué significa `⪯` para intervalos: **menor o igual en los dos extremos**, el
inferior y el superior.

### 9.2 Lo que se encontró: cuatro desigualdades que se comprueban a mano

**Primero, la transcripción, antes de afirmar nada.** Si hemos copiado mal el
problema, todo lo demás sobra. Se comprobó de dos maneras, las dos contra el
propio artículo. La segunda es la buena: **recalculando G en el x⋆ que ellos
imprimen** sale

    calculado por nosotros:   ([1.736721, 3.677497],  [1.393317, 6.731112])
    impreso en el artículo:   ([1.736722, 3.677497],  [1.393317, 6.731112])

Coinciden hasta el último dígito impreso en los cuatro valores. **Leemos su
problema como ellos lo leen.**

**Ahora el punto.** Tomamos

    y = (2.897500, 2.397500)

que está dentro de su caja. Y comparamos, en aritmética racional exacta, contra
los valores que **el propio artículo imprime** para x⋆:

    coordenada     G(y)        G(x⋆) impreso     margen        ¿menor?
    G_1 inferior   1.414351    1.736721          +0.322370     sí
    G_1 superior   3.403503    3.677497          +0.273994     sí
    G_2 inferior   1.119351    1.393317          +0.273966     sí
    G_2 superior   4.712655    6.731112          +2.018457     sí

**Los cuatro estrictamente menores.** Por tanto `G_i(y) ≺ G_i(x⋆)` en los dos
objetivos, y **x⋆ no es un punto Pareto óptimo de I-BK1 bajo su propia definición
2.17**, ni siquiera débilmente Pareto óptimo bajo su definición 2.16.

**Esto es lo que hay que enseñar en la diapositiva.** Cuatro números contra cuatro
números. No hace falta creerse nada del proyecto: los de la derecha son los que
el artículo imprime, y los de la izquierda se recalculan con una calculadora en
dos minutos.

**Y no es un artefacto del redondeo.** El más ajustado de los cuatro márgenes es
0.273966. Perturbar x⋆ en 10⁻⁶ en cada coordenada — que es más de lo que sus seis
decimales dejan abierto — mueve cualquiera de los valores como mucho 4×10⁻⁶, que
es **cinco órdenes de magnitud más pequeño** que ese margen.

### 9.3 Los solvers lo reproducen a ciegas

Esto es lo que convierte el hallazgo en algo que no depende de nuestra álgebra.

**"A ciegas" significa esto, literalmente:** la sesión que corrió los solvers
sobre I-BK1 recibió el problema y los tres φ y **nada** sobre el punto x⋆. La
pregunta que se le hizo no era la del apartado anterior. Era: corre los tres
solvers, y mira si devuelven puntos que ganen a la fila impresa del artículo,
según la definición 2.2 del propio artículo — que no depende de qué φ dirigió la
búsqueda.

**Los devuelven en todas las configuraciones.**

    configuraciones con un dominador       18 de 18
    semillas con un dominador, cada una     5 de 5
    puntos dominadores, mediana, a 5000     de 5 a 15
    puntos dominadores, mediana, a 20000    de 4 a 40
    mejor margen conseguido                 0.269627

Y ese mejor margen conseguido por un solver, 0.269627, contra el **0.273966** que
la derivación encontró algebraicamente por búsqueda exhaustiva. Dos rutas, dos
aritméticas, la misma respuesta.

### 9.4 Por qué el algoritmo del artículo se para donde se para — DECIR

Un fallo de una comprobación externa que no se explica es indistinguible de una
derivación mal hecha, así que se buscó el mecanismo y se encontró.

El artículo define "punto Pareto crítico" (su definición 2.18) con una condición
sobre direcciones de descenso, y esa condición se escribe con una **suma de
productos de intervalos**. Sumar intervalos término a término **pierde la
correlación** entre las coordenadas: el extremo superior de la suma sale al menos
tan grande como el peor de los dos casos, y estrictamente mayor cuando los dos
gradientes frontera no van en el mismo sentido.

La consecuencia: **exigir que el intervalo entero sea negativo es estrictamente
más fuerte que exigir que las dos funciones frontera bajen.** Así que puede haber
un punto sin ninguna dirección de descenso *intervalar* y que aun así tenga una
dirección que baja las cuatro columnas a la vez.

Y en I-BK1 eso se puede calcular en forma cerrada. El conjunto crítico del
artículo es `ν ∈ (1/9, 10)`, de medida **16.07** sobre la misma caja donde los
tres conjuntos eficientes miden 2.88, 3.79 y 5.69:

    **el conjunto crítico es 4.24 veces el conjunto eficiente de φ_lu, y
    contiene estrictamente a los tres.**

La forma cerrada se comprobó contra un barrido bruto de direcciones, calculado a
partir de los gradientes que el propio artículo imprime: doce puntos de prueba
repartidos por el cuadrante, incluido x⋆ y puntos a los dos lados de las dos
fronteras, contra un barrido de 60000 direcciones. **Cero desacuerdos.**

Y encaja con lo que el propio artículo publica: x⋆ está en ν = 0.110854 contra la
frontera 1/9 = 0.111111 — es decir, **justo fuera del conjunto crítico**, que es
consistente con su propio residuo publicado, −2.8154e−07 contra su tolerancia
10⁻⁶. **x⋆ es la salida del algoritmo en tolerancia, acercándose a un conjunto que
es cuatro veces demasiado grande.**

### 9.5 Qué se afirma y qué no — DECIR

**Ésta es la parte que hay que tener memorizada**, porque es la que decide si el
hallazgo es sólido o temerario.

**Se afirma, porque se comprobó:** dos resultados impresos del artículo — su
Proposición 2.1 y su Lema 2.4(ii), los dos en la página 7 — **son falsos tal como
están impresos**, y su propio primer problema de prueba es el contraejemplo. El
testigo es `x = (5/2, 5/6)`, estrictamente dentro del conjunto crítico. **Todas
las hipótesis se verificaron en lugar de suponerse**: el conjunto factible es
convexo; la diferenciabilidad se establece con dos resultados publicados de otro
artículo; el hessiano es definido positivo con las entradas que el propio [16]
imprime; la convexidad se comprobó directamente sobre 200000 cuerdas aleatorias
con cero violaciones; y la criticidad con un barrido de 200000 direcciones sin
encontrar ninguna. Y ese punto está dominado en las cuatro coordenadas por
`y = (1.886667, 1.440000)`, con margen mínimo 0.124351.

**No se afirma dónde falla la demostración. Y ésta es la frase que hay que decir
literalmente si preguntan:**

    La demostración de la Proposición 2.1 dice, en el artículo, que es "similar a
    la del apartado (ii) del Lema 2.4". Y el Lema 2.4 está atribuido a otro
    artículo de los mismos autores, de 2025, que **no tenemos**. Así que los dos
    fallos son en realidad uno solo, es heredado y no original de este artículo,
    y **no hemos leído la demostración que tendríamos que señalar**. Decimos que
    la conclusión es falsa; no decimos por qué.

**Y tampoco se afirma nada más.** Nada sobre su método de Newton, que puede
converger exactamente como dicen sus teoremas a exactamente lo que define su
definición 2.18. Nada sobre los otros diecinueve problemas de su apéndice. Nada
sobre su trabajo numérico más allá de los dos resultados impresos que se nombran.

**Dos obligaciones que esto le impone a la memoria**, y son vinculantes:

    la memoria **no puede citar** la Proposición 2.1 ni el Lema 2.4(ii), en
        ninguna forma, ni como justificación del estatus de un punto publicado.
    el x⋆ de la Tabla 1 **no puede usarse** como fixture, como checkpoint ni como
        punto de referencia en ninguna parte del proyecto.
    **el checkpoint publicado que sí vale, se usa**: es la curva de la ecuación
        (25), que cae dentro de las tres cuñas a lo largo de toda su longitud.

De paso salió un erratum menor: en su Tabla 2, la fila α = 0.8 lleva la segunda
coordenada de la fila α = 0.9, y los valores de esa fila se calcularon a partir
del valor mal impreso.

### 9.6 Por qué esto vale la pena tenerlo — DECIR

Ésta es la respuesta a "¿y esto para qué sirve?", y hay que darla sin
triunfalismo.

**Salió de aplicar el método, no de buscar errores.** El proyecto no se puso a
auditar ese artículo. Se puso a derivar el conjunto eficiente de uno de sus
problemas, porque necesitaba un problema intervalar de origen con respuesta
exacta. Y para poder fiarse de su propia derivación, buscó comprobaciones
externas: dos, de las que **una pasa y otra no**. El contraejemplo es la que no
pasa, investigada hasta el fondo en lugar de ignorada.

**Y es la mejor prueba de que la disciplina de verificación valía la pena.** Todo
el proyecto está construido sobre una regla incómoda — no se afirma nada que no
se haya comprobado contra la página impresa, y lo que no cierra se para en lugar
de parchearse. Esa regla cuesta tiempo en cada sesión y no produce resultados
visibles. **Aquí produjo uno**: un checkpoint que no cuadró, que en un proyecto
menos estricto se habría atribuido a un error propio y se habría ajustado hasta
que cuadrase.

    Dónde mirar. docs/part2/f2_ibk1_derivation.md, sección 4.2 para las cuatro
    desigualdades y la robustez al redondeo, y sección 4.3 para el mecanismo y el
    conjunto crítico. docs/part2/f3_native_run.md sección 6 para la reproducción
    a ciegas, con los datos en results/part2/dominators_summary.csv y
    results/part2/dominators_by_seed.csv. Y docs/part2/part2_closing.md sección
    5, que es la versión asentada y la que va a la memoria.


## PARTE 10. Cuatro trampas de diseño, y cómo se detectan — DECIR

Ésta es la mejor respuesta a "¿y cómo sé que algo de esto está bien?". Son
cuatro, en tres frases cada una: qué pasa, cómo se detecta y qué está en juego.

**A ninguna de las cuatro llega una revisión; a las cuatro llega una medida.**
Ésa es la parte que importa, porque una revisión sólo encuentra lo que ya
sospechas.

### 10.1 El modelo de anchura constante, con el que el estudio mide cero

**Qué pasa.** Convertir `f(x)` en `[f(x) − ε, f(x) + ε]` con ε constante deja
constante el segundo número de dos de los tres φ, y un campo constante no ordena
nada.

**Cómo se detecta.** Midiéndolo antes de construir nada encima. Los cuatro
conjuntos — los tres φ y el problema sin incertidumbre — salen **idénticos como
conjuntos de índices**, no sólo del mismo tamaño, en ZDT1 con 30 variables y
DTLZ2 con 12, sobre 5000 puntos. Y no hace falta que sea constante: con
imprecisión proporcional, donde la anchura varía muchísimo, la correlación entre
centro y anchura sale +1.0000 y los cuatro conjuntos vuelven a ser idénticos.

**Qué está en juego.** **Todas las tablas de la parte 1 habrían sido tablas de
unos**, y la conclusión habría sido "el orden no importa" — que es exactamente lo
contrario de lo que es verdad. Un estudio diseñado así no mide nada. Es la peor
de las cuatro con diferencia.

### 10.2 La anchura de ZDT1, cuyo óptimo cae donde están las soluciones

**Qué pasa.** La anchura natural para ZDT1 pasa todas las comprobaciones que el
propio proyecto prescribía: su recorrido es 0.4999, su correlación con el centro
es −0.011 y +0.103, y los tres φ separan. Por la comprobación prescrita es una
buena construcción, y no lo es.

**Cómo se detecta.** Repitiendo la comprobación **en la rodaja donde vive de
verdad el conjunto eficiente**, en lugar de sobre la caja entera. Allí el
conjunto de φ_cw es **exactamente** el conjunto sin incertidumbre, y los de φ_lu
y φ_ls son la rodaja entera. La causa es de alineación: la función que hay que
minimizar y la anchura se minimizan en el mismo sitio, así que no hay nada que
intercambiar.

**Qué está en juego.** Un estudio que informa de separación justo donde los
conjuntos coinciden. Y la lección tiene alcance general: **una muestra uniforme
de una caja de treinta dimensiones no contiene prácticamente nada cerca del
conjunto eficiente**, así que separar sobre ella no es evidencia. Esto se
convirtió en el criterio 3 de la puerta de la parte 2.

### 10.3 La cancelación en coma flotante que destruye la columna de la anchura

**Qué pasa.** Calcular la anchura como `(c + r) − (c − r)` no da `2r` en coma
flotante. El error es proporcional al tamaño del centro y cae entero en la
columna de la anchura, que es el segundo número de dos de los tres φ.

**Cómo se detecta.** Contando valores distintos. Una anchura que de verdad toma
**46** valores distintos en una rejilla sale con **210**. Y midiendo el error
contra una referencia en aritmética entera: 7.2e-16, 1.1e-13, 1.1e-10 y 1.1e-07
según el centro crece de 0 a 10⁹, mientras la ruta buena se queda en 2.2e-16 en
los cuatro casos.

**Qué está en juego.** No es el tamaño del error, es lo que le hace a la
estructura: **un orden construido sobre una columna está construido sobre los
empates de esa columna**, y la resta los rompe todos. Se arregla sin tolerancias:
componer φ con el cambio de representación da el mismo automorfismo leído en
otras coordenadas, comprobado entrada por entrada en racionales exactos sobre
2000 juegos de coeficientes. **Cada problema declara en qué representación está
calculado y φ se aplica una sola vez por la ruta que corresponde.** Por eso el
proyecto usa una única relación de dominancia sin tolerancia en todas partes.

### 10.4 La aserción de puerta que es imposible de satisfacer

**Qué pasa.** Asertar que la distancia del frente del solver al conjunto deducido
mejora al subir el presupuesto no se puede cumplir nunca, y hay un teorema que
dice por qué: el punto que causa la distancia está *protegido* (nadie puede
dominarlo, porque minimiza estrictamente una columna que depende de una sola
variable), así que un presupuesto mayor **lo vuelve a elegir** en lugar de
quitarlo, y su otra coordenada es libre.

**Cómo se detecta.** Escribiendo la proposición como proposición, con su
demostración de dos líneas, en lugar de dejarla como intuición. Y luego
midiéndola: al multiplicar el presupuesto por 80, la distancia al punto más
cercano cae por un factor de cuatro cada vez que el presupuesto se multiplica por
cuatro, **y el desbordamiento del punto protegido no se mueve**: 0.1226, 0.1404,
0.1334, 0.1261. Su valor esperado es exactamente 1/8, **a cualquier presupuesto**.

**Qué está en juego.** Una aserción que no puede pasar nunca, en la puerta que
decide si empieza la fase de experimentos: o se relaja la tolerancia hasta que
pase — que es ajustar el criterio a la fuerza del resultado — o bloquea el
proyecto por un motivo inexistente. Es la más sutil de las cuatro y la que mejor
enseña la disciplina: **la proposición y la aserción que la contradice caben en
el mismo documento.**

    Dónde mirar. 10.1 y 10.2 en docs/part1/a1_uncertainty_model.md, partes 1 y 2,
    y resumidos en docs/part1/part1_closing.md secciones 6.1 y 6.2. 10.3 en
    docs/part1/a4b_dominance_tolerance.md y en part1_closing sección 6.3. 10.4 en
    docs/part1/c3_validation.md, sección 1: la proposición está en 1.1, el
    corolario en 1.2 y la medida en 1.3.


## PARTE 11. Dónde está el proyecto y qué queda — DECIR

Hoy es 6 de septiembre. La presentación es el 25. Quedan diecinueve días.

### 11.1 Qué está hecho

**Las dos partes están cerradas.** La parte 1 (el marco, la calibración, los
benchmarks) está cerrada en `docs/part1/part1_closing.md`. La parte 2 (los
problemas intervalares de origen, I-BK1, el contraejemplo) está cerrada en
`docs/part2/part2_closing.md`. Los dos son documentos **canónicos**: son de donde
se levantan la memoria y el artículo, y están escritos para que no haya que abrir
nada más para los resultados.

Las seis fases están hechas. Hay 1074 tests, de los que 1062 pasan y 12 fallan a
propósito y de forma estricta. Todos los números de los tres registros de tirada
están generados, no tecleados.

**La afirmación final, que es lo que se defiende**, tiene dos párrafos y está
escrita palabra por palabra en `docs/part2/part2_closing.md` sección 8.3. En
resumen: la elección del orden no es un detalle de modelado, **bajo una condición
sobre el modelo de incertidumbre que el proyecto midió en lugar de suponer**; y
el efecto no es un artefacto de problemas construidos para exhibirlo, porque
reaparece sobre un problema publicado por otros. **Y lleva pegada una concesión
que no se puede quitar al comprimir**: en el problema publicado los tres
conjuntos se anidan en lugar de cruzarse, así que la magnitud de la parte 1 no
tiene equivalente allí y no se reclama ninguna.

### 11.2 Qué queda, y cuál es el entregable de verdad

Los entregables son tres, y con diecinueve días por delante conviene decir en voz
alta dónde va el esfuerzo:

    **la presentación es el entregable de verdad.** Es lo que ocurre el día 25 y
        es lo único con fecha y hora. La parte 13 de este documento es su guion.
    **este documento es la memoria informal.** Cubre el proyecto entero en
        lenguaje llano, con la procedencia de cada afirmación, y se monta desde
        aquí y desde los dos documentos de cierre.
    **el artículo es la salida formal, si da tiempo.** El material está: los dos
        documentos de cierre están escritos para que se levante de ellos.

El estudio de carteras es trabajo futuro, que es donde la diapositiva 21 de los
propios tutores lo pone.

### 11.3 Las cuatro cosas que el proyecto no hizo y sabe que no hizo

Ordenadas por lo que aportarían, y ninguna cabe antes del 25.

**1. Un segundo problema intervalar de origen: I-IKK1.** Dos sesiones. Es lo más
valioso que la parte 2 no hizo, y la razón está en la sección 8.4: **separa las
dos explicaciones** del anidamiento, cosa que ningún otro problema puede hacer.
Además daría un tercer punto de calibración, que es lo que convertiría dos
factores de error en una afirmación sobre el instrumento. Lo que no tiene es
checkpoint publicado: I-BK1 es el único del apéndice que lo tiene.

**2. La pregunta de la geometría.** Por qué en p1 dos conjuntos se cruzan y en
I-BK1 los tres se anidan. Lo que queda por descartar es la alineación de la
anchura, y **la medida que lo decidiría es concreta**: trasplantar el diseño de
anchura de p1 a ZDT1. Es una variante, no una familia nueva de problemas. Va a
trabajo futuro de la memoria.

**3. x-02.** Veinte semillas de búsqueda aleatoria sobre p1 bajo el Ejemplo 2.4.
**Es la medida más barata del proyecto** — el mismo código que e1 ya corrió — y
cierra una predicción registrada. Nadie la ha corrido.

**4. La curva de sensibilidad.** Interpolar entre el Ejemplo 2.2 y el 2.4 da
automorfismos admisibles por la propia definición del artículo, y el código está
construido para que sea un bucle. La diferencia en lo que se puede afirmar es
grande: "tres órdenes dan respuestas distintas" lo espera cualquiera que lea el
artículo; "el conjunto se mueve de forma continua a lo largo de la familia
admisible, y aquí está la curva" es un resultado que nadie ha producido sobre su
marco. **Fue lo primero que se recortó por calendario**, y sigue siendo la mejora
más grande disponible.

Y siguen abiertas las nueve preguntas a los tutores de la sección 7.2, de las que
sólo una (s-12) cambiaría un número.

    Dónde mirar. PROGRESS.md sección 1 para el estado actual, sección 2 para el
    estado de cada subparte y sección 7 para los riesgos abiertos.
    docs/part2/part2_closing.md sección 8.4 para lo que sigue abierto entre las
    dos partes, y sección 7.2 para la valoración de I-IKK1.


## PARTE 12. El mapa de ficheros — FONDO

No es un listado del repositorio. Está organizado por **la pregunta que alguien
podría hacerte**, y la respuesta es el fichero y el sitio dentro del fichero.

**"¿Dónde está la prueba de que los tres órdenes dan conjuntos distintos en p1?"**
`docs/part1/b1_phi_efficient_sets.md`, sección 2.4: las tres fórmulas cerradas.
Los números salen de `results/tier0/exact_regions_p1.csv`. La figura es
`results/meeting/derived_regions_p1.png`.

**"¿De dónde sale el número que has puesto en la diapositiva?"**
`docs/part1/part1_closing.md` sección 3.1 para todo lo de la parte 1, y
`docs/part2/part2_closing.md` sección 3.1 para lo de I-BK1. Las dos secciones
nombran el fichero `.csv` de cada cifra, columna por columna.

**"¿Dónde están los números crudos de los experimentos?"**
`results/tier0/` (p0 y p1), `results/tier1/` (ZDT1 y DTLZ2) y `results/part2/`
(I-BK1). En cada uno: `table_1_exact_*.csv` los valores deducidos,
`table_2_measured*.csv` los medidos, `table_3_solvers*.csv` los solvers,
`*_by_seed.csv` los valores por semilla, y `raw/` los arrays tal cual.

**"¿Cuánto se equivoca vuestro instrumento?"**
`results/tier0/instrument_error_p1.csv` y
`results/part2/instrument_error_ibk1.csv`. Son los dos únicos ficheros del
proyecto que ponen una cantidad deducida al lado de la misma cantidad medida.

**"¿Dónde está el contraejemplo?"**
`docs/part2/f2_ibk1_derivation.md`, sección 4.2 (las cuatro desigualdades) y 4.3
(el mecanismo). La versión asentada, que es la que va a la memoria, es
`docs/part2/part2_closing.md` sección 5. La reproducción por los solvers está en
`results/part2/dominators_summary.csv`.

**"¿Cómo vuelvo a correr los experimentos?"**
`python experiments/run_tier0.py`, `run_tier1.py` y `run_native.py`. Los tres
tienen `--seeds`, `--budgets` y `--record`, y por defecto escriben en `results/`
y regeneran su propio registro en `docs/`. Los tests son
`python -m pytest -q -m "not slow"` para la tirada rápida y `python -m pytest -q`
para la completa, que es la que hay que pasar antes de cada commit.

**"¿Dónde se decidió tal cosa?"**
`PROGRESS.md` sección 3 lleva las decisiones tomadas (filas d-nn). `docs/answered.md`
lleva las preguntas cerradas y los riesgos retirados, **con el razonamiento que
los retiró**, y no se borra nada: una fila se conserva con su historia.

**"¿Qué está abierto ahora mismo?"**
`PROGRESS.md`: sección 1 el estado, sección 6 las preguntas a los tutores,
sección 7 los riesgos, sección 9 las predicciones registradas.

**"¿Qué le vas a preguntar a los tutores?"**
`docs/supervisor_questions.md`. Tiene el texto completo de cada pregunta abierta,
con la hipótesis sobre la que se avanza mientras tanto y qué cambiaría cada
respuesta posible. Está escrito para poder contestarse de una sentada.

**"¿Por qué no comparáis los φ con hipervolumen, como todo el mundo?"**
La cabecera de `src/metrics_objective.py` y la de `src/metrics_decision.py`. Las
dos empiezan explicando para qué sirve esa familia y para qué no, y la segunda
dice por qué es la que lleva el resultado.

**"¿Qué dice exactamente el artículo de tus tutores?"**
`docs/part1/a0_framework.md`: la lectura afirmación por afirmación, con página y
número de ejemplo. Y `docs/verified.md`, que es la lista completa de hechos
verificados, v-01 en adelante.

**"¿Por qué fallan doce tests?"**
`docs/part1/c3_validation.md` sección 5 explica el hallazgo, y la 4.1 explica por
qué no se eximió a NSGA-II de la aserción. Los doce están fijados en
`tests/test_validation.py` como `xfail(strict=True)`.

**"¿Qué problemas publicados mirasteis, y por qué usasteis sólo uno?"**
`docs/part2/lit_review.md`, sección 1.8 (la tabla de los veinte problemas) y 1.9
(el veredicto criterio por criterio). Esa tabla va a la memoria pase lo que pase:
es lo que acredita que el corpus se leyó.

**"¿Qué figuras hay?"**
`results/meeting/derived_regions_p1.png` es la imagen de la parte 4 y es la que
resume el proyecto entero. `results/tier0/figures/` y `results/tier1/figures/`
llevan las de la parte 1, y `results/part2/figures/` las 24 de I-BK1, donde los
paneles de espacio de decisión a presupuesto 5000 son los que enseñan el
anidamiento.

**"¿Qué NO se puede decir?"**
`docs/part1/part1_closing.md` sección 8 y `docs/part2/part2_closing.md` secciones
8.5 y 9. Son las listas explícitas de conclusiones prohibidas, y están escritas
porque son fáciles de sacar por error de las tablas que sí están.

**"¿Cuál es la afirmación final, palabra por palabra?"**
`docs/part2/part2_closing.md` sección 8.3. Dos párrafos. El primero es de la
parte 1 y el segundo de la parte 2, y la última frase del segundo es una
concesión que no se puede quitar.


## PARTE 13. Esqueleto de la presentación — FONDO

**Esto no es la presentación.** Es el guion desde el que se construye, y su
utilidad es que la presentación se **monte** en lugar de inventarse. Cada línea
es una sección SLIDE de este documento, en el orden en que se cuenta, con qué
enseña la diapositiva y qué se dice encima.

Objetivo: **quince minutos**, unas quince diapositivas, un minuto cada una. Si
hay que recortar, se recorta desde la 12 hacia atrás, nunca del medio.

**Lo que la presentación NO lleva**, y esto está decidido y conviene respetarlo:
pymoo, semillas, tolerancias, la suite de tests, las reglas de cardinalidad, el
modo de muestreo del frente de referencia, y todos los identificadores de
subparte (a1, c3, e2, f2...). Si sale en preguntas, se contesta; en la
diapositiva, no.

    #   sección     qué enseña la diapositiva          qué se dice encima
    --------------------------------------------------------------------------

    1   Parte 1     Dos objetivos que se contradicen   "No hay un ganador. Hay un
                    y un frente de Pareto dibujado.    conjunto de compromisos, y
                                                       se llama conjunto eficiente."

    2   Parte 1.4   Un intervalo [38, 45] y la         "En la realidad los números
        + 2.1       pregunta: ¿[1,10] o [4,5]?         no son exactos. Y en cuanto
                                                       son intervalos, dejan de
                                                       poder ordenarse."

    3   Parte 2.2   Los tres φ, sus fórmulas, y la     "Tus tutores no propusieron
        + 2.3       analogía de la función clave.      un orden: describieron toda
                                                       la familia. Un φ es una
                                                       función clave, y cambiarla
                                                       cambia el resultado."

    4   Parte 2.5   La pregunta, en una línea.         "Cuánto cambia la respuesta
                                                       cuando lo único que cambia
                                                       es el orden. Y decir en voz
                                                       alta que no preguntamos
                                                       cuál es mejor, ni lo
                                                       contestamos."

    5   Parte 3.1   La tabla de los tres φ con ε       "Primer hallazgo, y es
        (A1)        constante, con los dos campos      metodológico. La forma obvia
                    constantes marcados.               de meter incertidumbre hace
                                                       que los tres órdenes
                                                       coincidan. Lo medimos antes
                                                       de construir nada encima."

    6   Parte 3.2   p1 y las tres fórmulas cerradas.   "Sobre un problema de dos
        (fase B)                                       variables se puede deducir
                                                       la respuesta exacta con sus
                                                       propios teoremas. Eso es lo
                                                       que hace posible todo lo
                                                       demás."

    7   Parte 4     LA IMAGEN.                         "Esto no es un resultado de
                    results/meeting/                   un algoritmo: son las tres
                    derived_regions_p1.png             fórmulas dibujadas. Fíjate en
                                                       que dos de ellas no se
                                                       contienen. Comparten el 10.3 %
                                                       de su unión."

    8   Parte 3.4   Las dos familias de métricas, en   "Esta es la idea que hay que
        (fase D)    dos columnas.                      entender. El hipervolumen no
                                                       puede comparar órdenes,
                                                       porque cada orden vive en
                                                       otro espacio. El espacio de
                                                       decisión es el mismo para
                                                       todos, y ahí sí."

    9   Parte 3.5   Una muestra, tres filtros, tres    "El control del experimento.
        (diseño)    conjuntos. Un diagrama.            La búsqueda aleatoria no
                                                       mira los objetivos, así que
                                                       los tres conjuntos difieren
                                                       SÓLO por el orden. Por eso el
                                                       resultado principal se mide
                                                       sobre ella y no sobre
                                                       NSGA-II."

    10  Parte 3.6.1 La tabla exacto contra medido,     "Y esto es lo que casi nadie
                    con el factor 1.81.                tiene: sabemos cuánto se
                                                       equivoca nuestro
                                                       instrumento. Exagera el
                                                       acuerdo en un factor 1.81."

    11  Parte 3.6.2 Los benchmarks, con la frase       "Como el instrumento exagera
        + 3.6.4     'del 63 al 91 %'.                  el acuerdo, estos números son
                                                       COTAS: los órdenes comparten
                                                       menos de lo que dice la
                                                       tabla."

    12  Parte 3.6.3 Las dos columnas de cardinalidad.  "Toda la dependencia con la
                                                       imprecisión es de un solo
                                                       conjunto. El otro está fijo,
                                                       y es demostrable en tres
                                                       líneas."

    13  Parte 8.1   La objeción, escrita como la       "Alguien va a decir que
        + 8.3       diría un crítico, y debajo         construimos el problema para
                    I-BK1 con sus corchetes.           que saliera. Tiene razón. Por
                                                       eso la parte 2 son problemas
                                                       publicados por otros, con los
                                                       intervalos en sus propios
                                                       coeficientes."

    14  Parte 8.4   Las tres cuñas y los seis          "Los tres órdenes vuelven a
                    extremos ordenados.                dar tres conjuntos distintos,
                                                       en forma cerrada. Pero aquí
                                                       se anidan en vez de cruzarse,
                                                       así que el número de antes no
                                                       tiene equivalente aquí, y no
                                                       lo reclamamos."

    15  Parte 9     LAS CUATRO DESIGUALDADES.          "Y esto salió de aplicar el
                    G(y) contra el G(x⋆) impreso.      método, no de buscar errores.
                                                       El punto que ese artículo
                                                       publica como Pareto óptimo
                                                       está dominado por éste, en
                                                       sus propios números. Los
                                                       solvers lo encontraron solos,
                                                       sin que se les dijera."

    16  Parte 11    La afirmación final y las tres     "Lo que queda, y por qué cada
        (cierre)    cosas que quedan.                  cosa está donde está."

**Notas de montaje.**

**La 7 y la 15 son las dos diapositivas que hay que clavar.** La 7 es el proyecto
entero en una imagen y la 15 es lo más memorable que salió. Si el tiempo se
tuerce, se sacrifica la 12 y luego la 6, nunca esas dos.

**La 15 admite dos versiones.** La corta es la tabla de cuatro filas y la frase
"los solvers lo reproducen a ciegas". La larga añade el conjunto crítico que es
4.24 veces demasiado grande. **Empieza por la corta**; el mecanismo es para las
preguntas, y hay que llevar preparada la frase de la sección 9.5 sobre lo que
**no** se afirma, porque es la primera pregunta que va a hacer un matemático.

**Ten a mano tres diapositivas de reserva**, sin numerar y fuera del recorrido:
las cuatro trampas de la parte 10, para "¿cómo sé que esto está bien?";
la contención de la sección 5.1, para la pregunta "¿y los tres pares?"; y la
pérdida de presión selectiva de la 5.3, para "¿y esto escala?".

**Y una frase de transición que hace falta y no ocupa diapositiva** (etiqueta
DECIR), entre la 11 y la 13: *la parte 1 midió sobre problemas que nosotros
adaptamos, y eso es una debilidad real; la parte 2 existe justamente para
responderla.* Decirlo tú antes de que lo digan ellos cambia el tono del resto.

    Dónde mirar. La lista de lo que la presentación excluye está en
    docs/plan_after_meeting.md sección g4, junto con los requisitos que deben
    existir antes de construirla. La afirmación, palabra por palabra, en
    docs/part2/part2_closing.md sección 8.3.


## Cierre

Tres cosas para terminar, que son las que conviene tener en la cabeza el día 25.

**Lo que el proyecto demuestra.** Que la elección del orden no es un detalle de
modelado — bajo una condición sobre el modelo de incertidumbre que se midió en
vez de suponerse, y que se puede comprobar en cualquier problema **antes** de
correr ningún algoritmo. Con la magnitud exacta en un problema, medida en dos
benchmarks con un instrumento cuyo error se conoce, y reproducida en un problema
publicado por otros.

**Lo que el proyecto no dice, y hay que ser el primero en decirlo.** No dice qué
φ es mejor: esa pregunta necesita un criterio externo que este proyecto no tiene.
No dice que los órdenes se aniden en los problemas intervalares de origen: eso es
un problema, con mecanismo localizado y explícitamente no general. Y no transporta
ningún factor de corrección a ningún sitio.

**Y lo que no se sabe.** La mitad del déficit de cobertura de NSGA-II no tiene
mecanismo después de descartar cinco por medición: **no sabemos por qué**. Por
qué en p1 dos conjuntos se cruzan y en I-BK1 los tres se anidan tiene un
mecanismo localizado pero no una demostración: **sabemos dónde mirar y no
sabemos la respuesta**. Y por qué el error del instrumento vale 1.81 en un
problema y entre 1.01 y 1.48 en otro es una propiedad de la geometría de cada
problema que nadie ha modelado.

**Que esas tres frases estén escritas es parte del resultado, no un defecto de
él.** Un trabajo que no tiene ninguna es un trabajo que no ha mirado lo bastante.
