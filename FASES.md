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


## estado

fases a, b y c completas. d1, d2 y d3 construidos; d3 pendiente de
revisión. e1 tirado y pendiente de revisión. 1013 tests, con doce parámetros en
xfail estricto que fijan el hallazgo de c3. lo siguiente es e3 sobre la salida de
e1, y a5-b antes de e2,
