# fases del proyecto

resumen corto de cada subparte: qué se hizo, qué archivo salió, qué se obtuvo, y
qué archivo de código con qué contenido. el plan de fases está en CONTEXT.md
sección 8; el estado vivo está en PROGRESS.md. lo último hecho es d3.


## fase a — formulación

### a0 revisión del marco teórico

docs/a0_framework.md. sin código.

19 afirmaciones del paper [1] (c1 a c19), cada una con su número de definición, teorema o ejemplo y su página impresa.

incluye la clase 𝔄_m y la condición de admisibilidad (determinante no nulo), los ejemplos 2.2,
2.3 y 2.4 con sus coeficientes exactos, la definición 3.1, los teoremas 3.1 a
3.3, los ejemplos 3.8 y 3.9 con la condición (15) escrita entera, y la función
trabajada que el paper da tras el ejemplo 3.9.

### a1 modelo de incertidumbre

docs/a1_uncertainty_model.md. sin código.

la decisión de cómo entra la imprecisión, se elige imprecisión en el objetivo con semianchura función del vector de decisión; se rechaza la imprecisión en los coeficientes (hace la semianchura función lineal del centro, que es la degeneración que anula el estudio) y la proporcional.

define p1 (caja [-0.5,1.5]^2, dos centros cuadráticos, semianchura rho·x_2^2 + delta) y la forma de tier 1, F_i = [f_i - r_i, f_i + r_i], con el caso crisp como eps = 0 exacto.

a1 rechaza tres variantes de anchuras distintas por objetivo, y las tres llevan
las dos semianchuras como funciones de la misma variable x_2 y opuestas en ella,
lo que hace incomparables todos los pares de puntos con x_2 distinto y devuelve
la caja entera bajo phi_ls y phi_cw. ese motivo de rechazo no alcanza a la
variante que a1-b mide después.

### a1-b anchuras distintas por objetivo, medida y adoptada

docs/a1_uncertainty_model.md, apéndice a1-b.

la variante que a1 no consideró: r_1 = rho·x_2^2 + delta y r_2 = rho·x_1^2 + delta,
las dos semianchuras no monótonas en variables distintas en lugar de opuestas en
una sola. medida y **adoptada**. es la forma que lleva src/problems_tier0.py y
sobre la que descansa entera la derivación de b1. bajo las anchuras idénticas de
a1 las dos columnas de anchura del problema transformado eran la misma función y
una de las cuatro no aportaba nada a la dominancia. sobre la rejilla de a1 el
conjunto eficiente de phi_cw resultó idéntico bit a bit, 961 puntos con el mismo
conjunto de índices, mientras phi_lu pasó de 527 a 460 y phi_ls de 1271 a 1505.

### a2 aritmética intervalar

src/interval_math.py.

add, scalar_multiply (con el intercambio de extremos si el escalar
es negativo), centre, half_width, width y gh_difference, sobre arrays de numpy.
centro, semianchura y anchura llevan tres nombres distintos porque el ejemplo
2.3 usa la anchura completa y el 2.4 la semianchura.

### a3 los tres phi

src/phi_transforms.py.

make_phi construye un phi desde sus coeficientes y valida la
condición del determinante; make_phi_of_centre_radius da el mismo phi leído en
coordenadas centro-radio; phi_registry contiene phi_lu, phi_ls y phi_cw como
registros no invocables, así el llamador nombra la ruta y no puede cruzarla.

el compuesto verificado sobre 2000 pares de coeficientes racionales.

### a4 problemas tier 0

src/problems_tier0.py.

p0, la función trabajada de [1], y p1, el problema de a1. cada uno
es un registro Problem con evaluate, representation ("endpoints" o
"centre_radius"), bounds, n_vars y n_obj. n_obj es m y nunca 2m.

docs/a4b_dominance_tolerance.md. mide el coste aritmético de
la ruta equivocada (46 valores de anchura convertidos en 210) y cierra dos
decisiones: d-02, una sola relación de dominancia sin tolerancia en todo el
proyecto, y d-01, delta = 1/8 en p1.

### a5 problemas tier 1

src/problems_tier1.py.

zdt1 y dtlz2 como problemas intervalares, en forma centro-semianchura desde el principio y sin construir ningún extremo. barrido de imprecisión con el caso crisp (eps = 0) como línea base degenerada.

### a5-b un driver de anchura por objetivo

src/problems_tier1.py, tests/test_problems_tier1.py,
docs/a1_uncertainty_model.md apéndice a5-b.

a5 daba a todos los objetivos de un problema la misma función de semianchura, así
que bajo los ejemplos 2.3 y 2.4 la imagen llevaba columnas duplicadas: zdt1 tenía
tres objetivos efectivos donde parece tener cuatro y dtlz2 cuatro donde parece
tener seis, y bajo el ejemplo 2.2 ninguno. **la duplicación es phi-dependiente** y
la comparación de cabecera del estudio es exactamente ese par, así que la
diferencia medida habría confundido el orden con la dimensión del problema
transformado. cada objetivo lleva ahora su propio driver, zdt1 r_1 en x_30 y r_2
en x_29, dtlz2 r_1, r_2 y r_3 en x_12, x_11 y x_10, **con la forma funcional de
cada semianchura sin tocar**, de modo que el argumento de a1 parte 4 se hereda en
vez de rehacerse.

la no-coincidencia se comprueba como propiedad y no como recuento: las 2m columnas
de la imagen son combinaciones lineales de las 2m funciones base con vectores de
coeficientes distintos dos a dos, cosa que se sigue solo de la condición de
determinante de [1], así que una coincidencia exigiría una dependencia lineal
entre las funciones base, y una matriz testigo de rango completo la descarta. la
anchura compartida de a5 falla el mismo certificado con rango 3 y rango 4.

el barrido de rodajas de a1 parte 4 se repitió sobre una rodaja que recorre todos
los drivers: **las dos formas pasan las cuatro condiciones en todos los niveles**,
y el arnés reproduce exactamente las dos tablas publicadas por a1 sobre la rodaja
de a1, que es lo que lo convierte en una repetición y no en un experimento nuevo.


## fase b — verdad de referencia

### b1 conjuntos phi-eficientes

docs/b1_phi_efficient_sets.md. sin módulo.

los conjuntos eficientes de p1 en forma cerrada bajo los tres phi.
convexidad por el teorema 3.3, regularidad por el criterio de [10], la
condición (15) convertida en un sistema lineal diagonal y resuelto como mapa
racional x(w). X_lu queda acotado por dos arcos cónicos, X_ls por uno y X_cw es
el cuadrado unidad cerrado salvo un lado. son regiones de dos dimensiones, no
curvas. p0 no cierra bajo ningún phi y queda como prueba de humo, no como
fixture.

### b2 frentes de referencia

src/reference_fronts.py.

codifica b1 y no deriva nada propio. efficient_set muestrea el
símplex de pesos y lo pasa por x(w); reference_front empuja ese conjunto por phi
y lo devuelve como array (k, 2m) en el mismo orden de columnas que producen los
solvers. include_singular_segments y sampling_mode no tienen valor por defecto.

docs/b2b_reference_density.md. el muestreo dirichlet reparte
la densidad según la parametrización de pesos y sesga el igd; se añade el modo
farthest_point y es el único válido para igd.


## fase c — solvers

### c1 búsqueda aleatoria

src/random_search.py.

sample_decision_space no toma phi, así que la muestra depende solo de la caja, el presupuesto y la semilla;
filter_one_sample_under_every_phi filtra una misma muestra bajo los tres phi, y
es el único punto del diseño donde el efecto del orden queda separado del efecto
de la búsqueda. define también non_dominated_indices, la única relación de
dominancia del proyecto.

### c2 nsga-ii y mopso

src/runners.py.

envuelve nsga-ii y mopso_cd de pymoo sin reimplementar nada.
TransformedProblem es el problema real de 2m objetivos que autoriza el teorema
3.1. el presupuesto se gasta en evaluaciones y no en generaciones, para que los
tres solvers tengan el mismo.


### c3 puerta de validación

docs/c3_validation.md. 

tests/test_validation.py.

el veredicto sobre si los solvers recuperan los conjuntos
derivados. la tolerancia se deriva antes de las tiradas, como distancia de
relleno de un frente de 100 puntos. la puerta falla en 12 de 90 medidas, todas
de nsga-ii, tres semillas bajo phi_ls y tres bajo phi_cw, ninguna bajo phi_lu.
ningún solver devuelve un punto que bata la derivación en 90 de 90, así que la
derivación, b2 y los tres solvers coinciden sobre dónde está el conjunto
eficiente. el fallo es un hallazgo (r-19: nsga-ii cubre peor que el muestreo
uniforme un conjunto eficiente de dimensión completa), no un defecto, y los doce
casos están marcados xfail estricto.


## fase d — análisis

### d1 métricas en el espacio imagen

src/metrics_objective.py.

compute_hv y compute_igd usando los indicadores de pymoo sin
normalizar, y compute_spread como M_3* de zitzler, deb y thiele.
derive_reference_point devuelve el punto junto con la regla que lo produjo;
igd_reference construye el frente de referencia con el modo y el flag a la vista;
common_cardinality y truncate_to_common_cardinality llevan todos los frentes de
una comparación a la misma cardinalidad. solo valen para comparar solvers bajo un
phi fijo, nunca para ordenar phi.

### d2 métricas en el espacio de decisión

src/metrics_decision.py.

las métricas comparables entre phi, porque el espacio de decisión
es el mismo para todos. compute_hausdorff, compute_coverage y compute_overlap
(ambas con delta explícito, sin valor por defecto), cross_evaluate, que filtra el
conjunto de un phi bajo el orden de otro, y compare_phi_on_one_sample. pair_status
marca los pares que involucran a phi_ls como comprobación y no como hallazgo, por
la contención de a-close. es la única subparte de la fase d en la ruta mínima.

### d3 tablas y figuras

src/reporting.py.

save_metrics_table escribe csv con las métricas de espacio imagen y
las de espacio de decisión en dos bloques de columnas distintas, cada uno con su
restricción escrita en el propio archivo,
read_metrics_table lo lee de vuelta. plot_fronts proyecta las 2m columnas por
pares y plot_decision_sets dibuja los conjuntos recuperados sobre la región
cerrada de b1 sección 2.4. plot_convergence no se construyó: runners.py no guarda
historia por generación.


## fase e — experimentos

### e1 tirada tier 0

experiments/run_tier0.py, tests/test_run_tier0.py, docs/e1_tier0_run.md.

los tres solvers, los tres phi, p0 y p1, sobre la lista de semillas, con
presupuesto 5000 y una comprobación de convergencia por problema a 20000, que es
la rejilla entera repetida. escribe los resultados crudos en results/tier0/, tres
tablas por save_metrics_table, dieciocho figuras por reporting y el registro, que
**se genera**: cada número del registro se lee de vuelta de un archivo que la
tirada escribió, que es la regla de procedencia de CONTEXT.md sección 10 e1.

tabla 1 exacta, solo p1: las áreas de las regiones de b1 sección 2.4 integradas en
forma cerrada, que reproducen las publicadas. tabla 2 medida, los dos problemas y
los dos presupuestos, sobre la muestra única filtrada de la búsqueda aleatoria,
con el suelo de ruido semilla a semilla del mismo phi al lado. tabla 3 los
solvers. **la diferencia entre la fila de p1 en la tabla 1 y en la tabla 2 es el
error del instrumento, medido una vez y solo aquí**: en el par libre en ambas
direcciones y a delta cero, la cobertura exacta 0.394710 se mide 0.555932 a
presupuesto 5000 y 0.504177 a 20000, y las tres cantidades del par se acercan a su
valor exacto al cuadruplicar el presupuesto.

tres cosas que el plan no había decidido. compute_overlap de d2 no es la fracción
compartida de la unión sino el coeficiente de dice, 0.187054 frente a 0.103177 en
el par de cabecera, así que la tabla 1 lleva la convención de d2 y
exact_regions_p1.csv lleva las dos. el suelo de ruido es una fila y no una
columna, porque el bloque de decisión de d3 no tiene columna para él. y **la
tolerancia no hace falta en el instrumento que lleva el resultado**: los tres
conjuntos de una comparación son conjuntos de índices sobre un mismo array, así
que a delta cero la cobertura es el recuento compartido exacto, y cada par se
reporta a delta cero además de a un veinteavo del diámetro de la caja.

m-1 y m-2, las dos medidas registradas en x-01 antes de la tirada, se calculan
aquí. e1 no las interpreta; eso es e3.


### e2 tirada tier 1

experiments/run_tier1.py, tests/test_run_tier1.py, docs/e2_tier1_results.md.

los tres solvers, los tres phi, zdt1_interval y dtlz2_interval, los cinco niveles
de imprecisión de src/problems_tier1.py, cinco semillas, con presupuesto 5000 y
una comprobación de convergencia por problema a 20000 en el nivel por defecto de
ese módulo: 108 configuraciones, 540 tiradas, 4243 segundos. escribe
results/tier1/, diez tablas por save_metrics_table —una por nivel y por tipo,
porque el bloque de decisión de d3 no tiene columna para el nivel—, 72 figuras y
el registro, que **se genera** como el de e1.

**no hay tabla 1 y el registro lo dice**: es exacta y solo de p1, y los dos
benchmarks no tienen forma cerrada, ni conjunto eficiente derivado, ni frente de
referencia, así que tampoco hay igd. lo que ocupa su lugar es el error del
instrumento de e1, leído de results/tier0/ y no tecleado: la cobertura exacta de
X_lu en X_cw es 0.394710 y se mide 0.555932 a presupuesto 5000 y 0.504177 a
20000, un sesgo relativo de 0.408 y 0.277. **el instrumento exagera el acuerdo**,
así que toda cobertura medida aquí es una cota superior del solapamiento
verdadero y una cota inferior de cuánto difieren los dos órdenes.

el par de cabecera, ejemplo 2.2 contra ejemplo 2.4, a delta cero y presupuesto
5000: en zdt1 la cobertura de X_lu en X_cw va de 0.846 a 0.545 al subir eps de
0.05 a 0.50 y la inversa de 0.088 a 0.160, con jaccard entre 0.087 y 0.133; en
dtlz2 de 0.898 a 0.684 y de 0.138 a 0.372, con jaccard entre 0.136 y 0.322. la
cobertura va primero por ser direccional, d-09, y el dice se imprime al lado del
jaccard porque los artefactos de e1 usan el primero.

**el suelo de ruido es exactamente cero en los dos benchmarks, en todos los
niveles y bajo los tres phi**, y eso es una medida y no una omisión: dos muestras
uniformes independientes no comparten ningún punto, y a treinta y a doce
variables una bola de un veinteavo del diámetro de la caja no contiene ninguno de
los puntos de la otra. el suelo se barrió para ver dónde deja de ser cero y es un
escalón, nunca un valor intermedio informativo: en zdt1 cero hasta un quinto del
diámetro y 0.438 a 0.896 a tres décimos; en dtlz2 0.0026 a 0.0066 a un décimo y
0.734 a 0.952 a un quinto. **a las dimensiones de tier 1 el suelo de la sección
b1 del plan no discrimina**, y la razón es la dimensión y no los problemas. el
barrido de delta dice lo mismo por el otro lado: la cobertura de cabecera no se
mueve nada entre delta cero y un décimo del diámetro, frente a p1, donde ese
mismo rango la llevaba de 0.556 a 0.997.

**la corrección de a5-b comprobada en la tirada y no heredada**: el número de
columnas efectivas es 2m bajo los tres phi en todos los niveles positivos y en
los dos problemas; en eps = 0 es m bajo el ejemplo 2.2 y m + 1 bajo los otros
dos, que es lo que hace de ese nivel una línea base. ninguna violación de la
contención en ningún sitio, r-11. r-20 se retira.

**el tamaño del rango 1 contra el tamaño de la población**, por configuración,
leído con un Callback de pymoo que deja el frente bit a bit idéntico: nsga-ii
satura en todas las semillas en las quince configuraciones de dtlz2 y en doce de
quince en zdt1; mopso en doce y en cinco. a eps = 0.10 nsga-ii llena las plazas
por primera vez en la generación 2 a 4 en dtlz2 y 4 a 17 en zdt1, que es el orden
de c3-d sobre las formas nuevas.

**m-2 con veinte semillas, el recuento que registra x-02**, calculada y no leída:
la mediana del voladizo es estrictamente positiva en zdt1 bajo los tres phi y en
dtlz2 bajo los ejemplos 2.3 y 2.4, y exactamente cero en dtlz2 bajo el ejemplo
2.2. se reporta contra dos estructuras, la registrada en x-01 y el propio
argumento de dominación de la sección f3 rehecho sobre las formas de a5-b, porque
a5-b movió qué variable lee cada semianchura. **m-1 no se calcula**, retirada en
la línea de resultado de x-01. e2 no interpreta nada de esto; eso es e3.


### e3 síntesis de resultados

docs/e3_synthesis.md. sin experimento, sin módulo y sin re-tirada: cada número
se lee de un fichero que escribió run_tier0.py o run_tier1.py y se nombra el
fichero al lado. **la parte 1 queda respondida.**

**la comparación que ninguna de las dos tiradas hizo**, que es la afirmación: e1
tiene los números exactos y ningún benchmark, e2 los benchmarks y ningún número
exacto. en una página: el jaccard exacto del par de cabecera en p1 es 0.103177 y
el mismo instrumento mide 0.187190 a presupuesto 5000, un factor de 1.81, así que
el 0.087 a 0.133 de zdt1 y el 0.136 a 0.322 de dtlz2 son cotas superiores y los
órdenes comparten menos de lo que imprimen las tablas.

**el signo del sesgo del instrumento se mide, no se supone.** si el sesgo fuera
un artefacto de muestra finita y no una propiedad de p1, los benchmarks tendrían
que responder igual al presupuesto sin tener valor exacto al que caer. lo hacen:
cuadruplicar el presupuesto baja los tres estadísticos en p1, dtlz2 y zdt1, nueve
de nueve. **la magnitud no se transfiere y no se aplica ningún factor de
corrección a ningún número de benchmark.**

**la dependencia de eps.** la cobertura de X_lu en X_cw baja de 0.846 a 0.545 en
zdt1 y de 0.898 a 0.684 en dtlz2; el jaccard sube, y las dos cosas salen de la
columna de cardinalidad. |X_cw| es 257 y 1813 en **todos** los niveles positivos,
porque eps entra en la imagen del ejemplo 2.4 solo como escalar positivo sobre
las columnas de anchura y un reescalado positivo no cambia la relación de pareto.
toda la dependencia de eps del par de cabecera es de X_lu. **estaba predicho**,
en la parte 4 de docs/a1_uncertainty_model.md, y se confirma aquí sobre la
cardinalidad de la tirada y no sobre una fracción de rodaja, r-22.

**la forma, que la magnitud esconde.** en p1 los dos conjuntos no se contienen en
ningún sentido, 0.394710 y 0.122571; en tier 1 X_lu está en gran parte dentro de
un X_cw mucho mayor. misma magnitud de desacuerdo, geometría distinta. la
distancia de hausdorff simétrica normalizada es el único estadístico estable a
dos, doce y treinta variables, 0.29 a 0.39, y **no está calibrada**.

**el suelo de ruido se retira medido y no se omite**, por una razón estructural y
no de tier 1, y lo que ocupa su lugar ya está en las tablas: la cobertura de
cabecera se calcula sobre UNA muestra filtrada tres veces, así que su rango
intercuartílico entre semillas es toda su variabilidad muestral. el criterio se
aplica por problema, nivel y par: **las ocho celdas de la dirección que sostiene
la afirmación pasan; cuatro de las ocho de la otra dirección fallan**, todas con
mediana cerca de 1.0 y X_lu pequeño.

**x-01 se cierra.** la cláusula de dtlz2 se confirma y por una comparación más
fina de la que pedía: bajo el ejemplo 2.4, sobre una muestra y un juego de
semillas, la columna cuyo conjunto libre es {x_2} mide exactamente 0.000000 y las
tres de conjunto libre de once variables miden 0.737 a 0.843, o sea que la
condición discrimina columna a columna **dentro de un mismo phi**. la cláusula de
zdt1 queda **no comprobable**: se registró contra las formas de a5 y a5-b movió
r_2 a x_29, así que el argumento de dominación de la sección f3 ya no se le
aplica. ni confirmada ni refutada. m-1 sigue retirada. **x-02 sigue abierta** y
e3 lo dice en vez de inventar un veredicto: es una medida de p1 y e2 tiró solo
tier 1.

**la pregunta de los solvers, respondida aparte y nunca mezclada con la
comparación de phi.** las veinticuatro configuraciones de nsga-ii con imprecisión
positiva saturan el rango 1 en todas las semillas, así que esos frentes son
resultados de dispersión y no de convergencia, y en tier 1 no hay ninguna medida
de convergencia por no haber frente de referencia. **el bloque objetivo de e1 no
responde a ninguna pregunta de solvers**, al estar a cardinalidad completa.

**la afirmación probada cláusula a cláusula.** el ataque que no se puede rebatir
es que el modelo de incertidumbre se eligió para separar, y **la afirmación
recomendada es condicional**, con la forma lineal rechazada de a1 como brazo
negativo medido. tres figuras nombradas para g2, una de ellas ya existe.


## estado

fases a, b y c completas. d1, d2 y d3 construidos; d3 pendiente de
revisión. **fase e completa por el lado de la parte 1**: e1 y e2 tirados, tier 0
y tier 1, a5-b hecho, y **e3 escrito**, con la parte 1 respondida en
docs/e3_synthesis.md y pendiente de revisión. doce parámetros en xfail estricto
fijan el hallazgo de c3. lo siguiente es g1, que ya tiene sus dos prerrequisitos,
con g2 al lado y f1 en paralelo, y luego g3 y g4.
