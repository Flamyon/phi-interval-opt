# Prompt: construir la presentación LaTeX (Beamer) del proyecto

Eres un agente que va a construir, desde cero, la presentación final de un
proyecto de investigación de tres meses sobre **órdenes de intervalos en
optimización multiobjetivo**. No has leído el repositorio. Este prompt te dice
qué leer, qué debe contener cada diapositiva, de dónde sale cada número, qué
está prohibido y cómo se entrega. Trabajas en el directorio raíz del
repositorio `phi-interval-opt`.

## 0. Datos fijos

- **Título del proyecto**: "Técnicas de Optimización Intervalar basadas en
  Inteligencia Computacional" (proyecto PI3, julio–septiembre 2026).
- **Autor / ponente**: Francisco Rodríguez-Carretero Roldán.
- **Tutores**: Antonio Beato Moreno y Rafaela Osuna Gómez.
- **Fecha de exposición**: 25 de septiembre de 2026.
- **Duración**: 15 minutos. **17 diapositivas de recorrido** + portada + 3 de
  reserva fuera del recorrido. Menos de un minuto por diapositiva.
- **Audiencia**: personas que **nunca han oído hablar del problema**. Saben
  matemáticas de grado y algo de programación. No saben qué es un frente de
  Pareto, ni un intervalo como valor de una función, ni un automorfismo φ.
  Todo concepto se introduce antes de usarse; las tres primeras diapositivas
  existen sólo para eso.
- **Idioma**: español. Los términos técnicos se dan en español con el nombre
  del artículo entre paréntesis la primera vez (p. ej. "conjunto eficiente
  (frente de Pareto)").
- **Herramienta**: LaTeX Beamer. En la máquina hay `pdflatex`, `lualatex`,
  `beamer` y el tema `metropolis`. Usa metropolis (o un tema igual de sobrio),
  relación de aspecto 16:9, `\usepackage[spanish]{babel}`, fuente legible a
  distancia. Nada de fondos oscuros ni decoración.
- **Fuente del guion**: `docs/explicacion_proyecto.md`. Es un documento largo
  en español escrito para el ponente. **Léelo entero antes de escribir una
  línea de LaTeX.** Sus secciones llevan etiqueta SLIDE / DECIR / FONDO: sólo
  las SLIDE van a diapositivas; las DECIR son notas del orador; las FONDO no
  entran. La **parte 13** de ese documento es el esqueleto de 17 diapositivas y
  es **el guion que vas a montar**, no uno que vas a inventar.

## 1. Qué leer, en orden

1. `docs/explicacion_proyecto.md` — entero. Es la fuente principal y basta
   para el 90 % del contenido. Cada sección termina en un párrafo "Dónde
   mirar" que apunta al fichero que produjo cada afirmación.
2. `docs/part2/part2_closing.md` sección 8.3 — la afirmación final, palabra
   por palabra. Y sección 12, la concesión añadida.
3. `docs/part1/e3_synthesis.md` sección 9 — las figuras que la presentación
   debe usar.
4. `docs/plan_after_meeting.md` sección g4 — la lista de lo que la presentación
   excluye y la regla de procedencia de los números.
5. `papers/Presentacion_optimizacion_intervalar.txt` — la propuesta original
   de los tutores (23 diapositivas, texto extraído). Sirve para dos cosas: ver
   el tono y las figuras que ellos ya usaron (el ejemplo A = [1.5, 5],
   B = [3, 7.5] de su diapositiva 4 se puede reutilizar tal cual), y para
   comprobar que la diapositiva 17 de ellos pide "búsqueda aleatoria como
   referencia base" y la 21 pone carteras como trabajo futuro.
6. Los CSV bajo `results/` que se nombran diapositiva a diapositiva más abajo.
   **Todo número que aparezca en una diapositiva se lee de uno de ellos.**
7. `CONTEXT.md` secciones 2 y 4 sólo si necesitas la definición formal de φ o
   la redacción exacta de la pregunta de investigación.

No hace falta leer `PROGRESS.md`, `FASES.md`, `docs/part1/session_log.md`,
`docs/part2/session_log.md` ni el código en `src/`, salvo para resolver una
duda concreta.

## 2. Vocabulario que hay que respetar

- Los tres órdenes se llaman **φ_lu (Ejemplo 2.2)**, **φ_ls (Ejemplo 2.3)** y
  **φ_cw (Ejemplo 2.4)** del artículo [1]. En las diapositivas usa las dos
  formas la primera vez y después la corta.
  - φ_lu: `[l, u] → (l, u)` — extremo inferior y superior.
  - φ_ls: `[l, u] → (l, u − l)` — extremo inferior y **anchura**.
  - φ_cw: `[l, u] → ((l+u)/2, (u−l)/2)` — centro y **semianchura**.
- **Anchura** (u − l) y **semianchura** ((u − l)/2) son palabras distintas y
  no se intercambian. φ_ls usa anchura; φ_cw usa semianchura.
- Los conjuntos eficientes bajo cada orden se escriben X_lu, X_ls, X_cw.
- El artículo del marco se cita **siempre con sus tres autores**:
  **[1] Costa, Osuna-Gómez y Chalco-Cano (2024)**, *Fuzzy Sets and Systems*
  477, 108812. Nunca "el artículo de los tutores".
- El artículo de la parte 2 se cita como **[16] Mondal, Ghosh y Kim (2026)**,
  arXiv:2603.06000, *Newton Method for Multiobjective Optimization Problems of
  Interval-Valued Maps*. Sus veinte problemas de prueba proceden, según [16]
  mismo, de Mondal y Ghosh (2025), *Numer. Algorithms*; si hay una diapositiva
  de referencias, cita los dos.
- Mantén la numeración [1], [7], [16] de la bibliografía de los tutores; no
  renumeres.

## 3. Lo que la presentación NO lleva (decidido; no negociable)

En ninguna diapositiva del recorrido: pymoo, semillas, tolerancias, la suite de
tests, "12 tests que fallan", reglas de cardinalidad, el modo de muestreo del
frente de referencia, `delta`, `include_singular_segments`, y **ningún
identificador de subparte** (a0, a1, b1, c3, e1, e2, f2, f5, f7, f8, g4…). Si
una figura existente lleva uno de esos identificadores en su título, se
regenera sin él.

Y estas prohibiciones de contenido, que el proyecto comprueba al cerrar cada
parte:

1. **Nunca se ordena ni se clasifica a los tres φ.** No hay "mejor φ". Ninguna
   frase, tabla ni color puede sugerir que uno es superior. La pregunta del
   proyecto es *cuánto cambia la respuesta cuando lo único que cambia es el
   orden*, y la diapositiva 4 lo dice en voz alta.
2. **El factor 1.81 no se transporta.** Es el error del instrumento en p1. No
   se puede dividir ningún número de ZDT1, DTLZ2 ni I-BK1 por 1.81 ni sugerir
   un "valor corregido".
3. **Las dos concesiones de la afirmación final no se pueden quitar al
   comprimir**: (a) en I-BK1 los tres conjuntos se anidan, así que el número
   de la parte 1 no tiene equivalente allí y no se reclama; (b) ser intervalar
   de origen no basta por sí solo para que el orden importe (I-VU2).
4. **No se cita la Proposición 2.1 ni el Lema 2.4(ii) de [16]** como apoyo de
   nada, y el punto x⋆ de su Tabla 1 no se usa como referencia de nada. Se
   nombran sólo en la diapositiva 16 como lo que el contraejemplo contradice.
5. La diapositiva del contraejemplo es **una corrección, no una crítica**. No
   se dice dónde falla su demostración (no se ha leído: está en otro artículo
   de 2025 que el proyecto no tiene). Se dice que la conclusión es falsa y
   cómo se comprueba.
6. No se afirma nada sobre "los problemas intervalares de origen como clase":
   un problema cruza (p1), otro anida (I-BK1) y otro iguala (I-VU2).

## 4. Regla de procedencia de los números

**Ningún número se teclea a mano en el `.tex`.** Escribe un script
`experiments/make_presentation.py` que:

- lea los CSV bajo `results/` que se listan en la sección 5,
- genere las figuras nuevas en `results/figures/presentation/` (PNG a 200 dpi
  o PDF vectorial),
- emita fragmentos LaTeX (tablas completas o macros `\newcommand`) en
  `results/figures/presentation/fragments/*.tex`, que el `.tex` de la
  presentación incorpora con `\input`.

Cada fragmento lleva un comentario LaTeX con el fichero y la clave de la que
sale. Redondea a **una cifra decimal en porcentajes** y a **tres decimales**
en fracciones cuando la diapositiva lo pida; el CSV conserva los seis. Las
fracciones exactas (4/5, 4/3, 3/4, 3/2, 2/3, 5/3, 1/2, 2) se escriben como
fracciones, no como decimales.

Excepción: las figuras **conceptuales** de las diapositivas 1, 2, 3 y 9 (frente
de Pareto genérico, recta con dos intervalos, esquema de la función clave,
diagrama "una muestra, tres filtros") no llevan datos del proyecto y se dibujan
en TikZ dentro del `.tex`.

## 5. Las diapositivas, una a una

Formato por diapositiva: **título** (una frase, no un tema), **qué se ve**,
**qué se dice** (va a `\note{}` como nota del orador, en español, en el tono
de las frases "se dice" de la parte 13 de `explicacion_proyecto.md`), y
**fuente**. Tiempo orientativo entre paréntesis; el total suma 15 minutos.

**Portada** (0:10). Título del proyecto, nombre, tutores, fecha, universidad.
Subtítulo opcional que ya diga de qué va: "¿Cuánto cambia la respuesta cuando
lo único que cambia es el orden?".

### Bloque A — el problema, para quien no lo ha oído nunca (3 min)

**1. Optimizar con varios objetivos** (0:50). *Se ve*: dos objetivos que se
contradicen (coste vs. riesgo, o rapidez vs. memoria de un programa) y un
frente de Pareto dibujado en TikZ: nube de puntos, los no dominados marcados.
La definición de dominancia en una caja: "A domina a B si es igual o mejor en
todos los objetivos y estrictamente mejor en al menos uno". *Se dice*: no hay
un ganador; hay un conjunto de compromisos, y se llama conjunto eficiente.
*Fuente*: `explicacion_proyecto.md` §1.1–1.3.

**2. Los números no son exactos, y los intervalos no se ordenan** (0:50).
*Se ve*: un intervalo `[38, 45]` con centro 41.5, semianchura 3.5 y anchura 7
etiquetados; debajo, en una recta, `A = [1.5, 5]` y `B = [3, 7.5]` (el ejemplo
de la diapositiva 4 de los tutores) y luego `A = [1, 10]` frente a `B = [4, 5]`
con la pregunta "¿cuál es menor?". *Se dice*: en la realidad el coste no es
40, es "entre 38 y 45"; y en cuanto los objetivos son intervalos, dejan de
poder ordenarse; no es un problema técnico, es que hay muchas formas válidas
y cada una es una decisión. *Fuente*: §1.4, §2.1.

**3. Una familia entera de órdenes: φ** (1:00). *Se ve*: la idea de [1] —
en vez de un orden, toda la familia, con un parámetro φ que dice cuál usas.
Un φ coge `[l, u]` y devuelve dos reales; dos reales sí se comparan. Los tres
φ con sus fórmulas en una tabla de tres filas (nombre del ejemplo, fórmula, qué
significa en palabras). Analogía en una línea: φ es la función `key` de un
`sort`; cambias la `key`, cambia el orden. Regla: m objetivos intervalares →
2m objetivos reales, y un problema real ya se sabe resolver. *Se dice*: [1]
no propuso un orden, describió la familia; los tres son válidos, los tres son
distintos, y cada uno da un conjunto eficiente distinto. *Fuente*: §2.2–2.4,
`CONTEXT.md` §4.

**4. La pregunta** (0:30). *Se ve*: una sola línea grande: "**¿Cuánto cambia
la respuesta cuando lo único que cambia es el orden?**". Debajo, en pequeño,
lo que NO se pregunta: "¿qué φ es mejor?" — necesita un criterio externo que
ningún benchmark tiene; cada φ vive en un espacio distinto. *Se dice*: que no
lo preguntamos y no lo contestamos. *Fuente*: §2.5.

### Bloque B — método y resultado sobre problemas controlados (6 min)

**5. Primer hallazgo: la forma obvia de meter incertidumbre no mide nada**
(1:00). *Se ve*: `f(x) → [f−ε, f+ε]` con ε constante; tabla de tres filas con
lo que devuelve cada φ y **el segundo campo resaltado como constante** en φ_ls
`(f−ε, 2ε)` y φ_cw `(f, ε)`. Frase: "un campo constante no ordena nada". Y la
regla que sale: la anchura tiene que estar movida por una variable que el
centro no determine; basta con que la anchura sea función exacta del centro
para que los tres órdenes coincidan (se midió: correlación +1.0000 y cuatro
conjuntos idénticos punto por punto). *Se dice*: es un hallazgo metodológico
y se midió antes de construir nada encima; con ese diseño todas las tablas
habrían sido tablas de unos. *Fuente*: §3.1 (A1), §10.1.

**6. Un problema donde la respuesta exacta se puede deducir a mano** (0:50).
*Se ve*: p1, dos variables en la caja `[−0.5, 1.5]²`, dos objetivos
intervalares escritos como centro ± semianchura:
`c_1 = x_1² + (x_2−1)²`, `r_1 = ¼ x_2² + ⅛`;
`c_2 = (x_1−1)² + (x_2−1)²`, `r_2 = ¼ x_1² + ⅛`.
Señalar que la semianchura de cada objetivo la mueve la variable del **otro**
(la regla de la diapositiva 5 aplicada). Y las tres regiones en forma cerrada,
en una línea cada una: X_cw = cuadrado unidad `[0,1]²`; X_ls = `[0, 4/3]²`
recortado por el arco `7x_1x_2 − 4x_1 + 12x_2 − 16 ≤ 0`; X_lu = lente entre
ese arco y `4x_1 − x_1x_2 − 20x_2 + 16 ≤ 0`, con x_2 ∈ [4/5, 4/3]. *Se dice*:
con el Teorema 3.3 y el Ejemplo 3.9 de [1] — sus propios resultados,
aplicados — se deduce exactamente el conjunto eficiente bajo cada φ; sin una
respuesta exacta no se puede preguntar cuánto se equivoca el instrumento.
*Fuente*: §3.2, `src/problems_tier0.py` (`evaluate_p1`),
`docs/part1/b1_phi_efficient_sets.md` §2.4.

**7. LA IMAGEN: un problema, tres órdenes, tres conjuntos** (1:00). *Se ve*:
la figura de las tres regiones exactas de p1, a página completa. Existe en
`results/meeting/derived_regions_p1.png`, pero su título lleva "b1 section
2.4" y está en inglés: **regenérala** con el script a partir de las tres
desigualdades de la diapositiva 6 (máscara sobre una rejilla fina de la caja),
con los tres puntos (0, 4/5), (4/3, 1), (0, 4/3) marcados, la intersección
X_lu ∩ X_cw rayada, leyenda en español y sin identificadores. Tres cifras al
pie: áreas 0.311 (lu), 1.000 (cw), 1.513 (ls); y "X_lu y X_cw comparten el
**10.3 %** de su unión". *Se dice*: esto no es la salida de un algoritmo, son
las tres fórmulas dibujadas; fíjate en que la lente y el cuadrado no se
contienen — cada uno tiene una zona a la que el otro no llega; el 60.5 % de
X_lu queda fuera de X_cw y el **87.7 %** de X_cw queda fuera de X_lu. *Fuente*:
`results/tier0/exact_regions_p1.csv` (claves `area`, `overlap_union_share`,
`coverage_a_in_b`, `coverage_b_in_a` sobre el par lu, cw); §4.

**8. Dónde se mide: dos familias de métricas** (1:00). *Se ve*: dos columnas.
Izquierda, *espacio de objetivos* (hipervolumen, IGD): sirve para comparar
algoritmos con un φ fijo; **no** sirve para comparar φ, porque cada φ manda el
problema a un espacio distinto con otra escala — "kilómetros entre
kilogramos". Derecha, *espacio de decisión* (cobertura, Jaccard, Hausdorff):
la caja de `x` es la misma para todos los φ, un punto `x = (0.3, 0.9)` es el
mismo bajo los tres; **aquí sí**. Definición de cobertura(A→B) en una línea,
con la nota de que es asimétrica y se dan las dos direcciones. *Se dice*: si
sólo se entiende una idea conceptual, es ésta; la pregunta no es qué frente
sale más bonito, es qué decisiones te quedan encima de la mesa. *Fuente*: §3.4.

**9. El diseño: una muestra, tres filtros** (0:50). *Se ve*: diagrama TikZ.
Una caja → 5000 puntos sorteados → una evaluación → tres filtros (φ_lu, φ_ls,
φ_cw) → tres conjuntos. Al lado, el contraste: NSGA-II con tres φ cambia dos
cosas a la vez (el criterio y la búsqueda). *Se dice*: la búsqueda aleatoria
no mira los objetivos para decidir dónde mirar, así que los tres conjuntos
difieren SÓLO por el orden; no es el rival flojo, es el instrumento que lleva
el resultado principal; NSGA-II y MOPSO están para comprobar la derivación y
medir lo que le cuesta a un algoritmo de verdad. Y que la propuesta de los
tutores (su diapositiva 17) ya pedía la búsqueda aleatoria como referencia
base. *Fuente*: §3.5.

**10. Cuánto se equivoca el instrumento** (0:50). *Se ve*: tabla de tres
filas, par φ_lu vs φ_cw en p1, presupuesto 5000: exacto / medido / error.
cobertura(lu→cw) 0.395 / 0.556 / +40.8 %; cobertura(cw→lu) 0.123 / 0.222 /
+81.0 %; Jaccard 0.103 / 0.187 / **×1.81**. Nota al pie: a 20000 los tres
errores bajan (+27.7 %, +48.6 %, ×1.49). *Se dice*: casi ningún trabajo
empírico tiene esto; el instrumento exagera el acuerdo, siempre hacia arriba,
y la razón es intuitiva (los puntos fáciles de encontrar son los compartidos).
*Fuente*: `results/tier0/instrument_error_p1.csv` (filas lu, cw, delta 0.0;
el Jaccard a partir de `overlap` por `jaccard = dice / (2 − dice)`) y
`results/tier0/exact_regions_p1.csv`.

**11. Los benchmarks: del 63 al 91 %** (1:00). *Se ve*: tabla de ocho filas
(ZDT1 con 30 variables y DTLZ2 con 12, ε = 0.05, 0.10, 0.25, 0.50) con
columnas: ε, 1 − cob(cw→lu) en %, |X_lu|, |X_cw|. Encima, la frase grande:
"**Entre el 63 y el 91 % del conjunto eficiente de un orden queda fuera del
del otro, en todos los niveles de imprecisión, en los dos benchmarks.**"
Fila de cordura mencionada en nota: con ε = 0 todo vale 1. *Se dice*: como el
instrumento exagera el acuerdo, estos números son **cotas**: los órdenes
comparten menos de lo que dice la tabla. Y decir que la otra dirección
(fracción de X_lu fuera de X_cw) también se midió y no se cita como cifra
porque no es estable entre semillas. *Fuente*:
`results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv`, bloque de
decisión, filas `lu,cw` con solver `finding`, métrica `coverage_b_in_a`,
`n_evals` 5000, delta 0.0, columna `median`; cardinalidades en las columnas
`cardinality` y `reference_size` de las mismas filas. Comprueba que los ocho
valores de 1 − mediana caen entre 0.628 y 0.912.

**12. Toda la dependencia con ε es de un solo conjunto** (0:40). *Se ve*: las
dos columnas de cardinalidad de la tabla anterior como dos series (gráfico de
barras o líneas, generado): |X_cw| plano (257 en ZDT1, 1813 en DTLZ2 en todos
los ε > 0) y |X_lu| creciendo (26→36→53→68; 278→351→575→980). Y el argumento
en tres líneas: bajo φ_cw la imagen es (centro, semianchura); ε multiplica las
semianchuras por una constante positiva; eso no cambia quién domina a quién.
*Se dice*: el conjunto de φ_cw no se mueve y es demostrable; el de φ_lu crece;
la dirección estaba predicha por escrito antes de correr. *Fuente*: mismas
filas que la 11; argumento en `docs/part1/e3_synthesis.md` §3.1.

> Transición hablada entre la 12 y la 13 (nota del orador, no diapositiva):
> "La parte 1 midió sobre problemas que nosotros adaptamos, y eso es una
> debilidad real. La parte 2 existe justamente para responderla."

### Bloque C — problemas publicados por otros (4 min)

**13. La objeción, y la respuesta: problemas intervalares de origen** (0:50).
*Se ve*: arriba, la objeción tal como la diría un crítico, entre comillas:
"Habéis construido el problema para que dé la respuesta que queréis. Con una
banda constante os habría salido cero, y lo sabéis porque lo medisteis."
Debajo: "Es verdad." Y el problema I-BK1 de [16] (problema 1 de su apéndice A)
con **los corchetes en los coeficientes** resaltados:
`G_1 = [0.1, 0.2] x_1² + [0.1, 0.3] x_2²`,
`G_2 = [0.1, 0.3] (x_1−5)² + [0.1, 0.5] (x_2−5)²`, caja `[−10, 10]²`.
*Se dice*: intervalar de origen significa que los intervalos son del propio
problema, publicados por otros autores para otro propósito; no elegimos ni el
ancho ni qué variable lo mueve; y se comprobó en racionales exactos que centro
y semianchura no son proporcionales (cocientes 1/3 vs 1/2 y 1/2 vs 2/3), así
que la no degeneración es de [16], no nuestra. Mencionar en una línea que
[16] tiene 20 problemas y que se cribaron con cinco criterios escritos antes
de abrirlo. *Fuente*: §8.1–8.3.

**14. I-BK1 en forma cerrada: tres cuñas anidadas** (1:00). *Se ve*: figura
generada de las tres cuñas en el plano (x_1, x_2), entre las hipérbolas
`ν = x_2(5−x_1) / (x_1(5−x_2))` = const, ancladas en (0,0) y (5,5); dibujar
la región `[0,5]²` (fuera de ella la respuesta no vive) sobre la caja. Al lado,
la línea `1/2 < 2/3 < 3/4 < 3/2 < 5/3 < 2` con cada extremo etiquetado con su
φ: X_cw: ν ∈ [3/4, 3/2] (área 2.876); X_lu: ν ∈ [2/3, 5/3] (3.790);
X_ls: ν ∈ [1/2, 2] (5.685). Frase: "X_cw ⊂ X_lu ⊂ X_ls, las tres estrictas;
el 49.4 % del mayor queda fuera del menor". *Se dice*: los tres órdenes
vuelven a dar tres conjuntos distintos, en forma cerrada, sobre un problema
que no construimos; pero aquí se anidan en vez de cruzarse, así que el número
del 63–91 % no tiene equivalente aquí y no lo reclamamos; y hay una
comprobación externa que pasa: la curva de la ecuación (25) de [16] tiene
ν = 162/169 constante y cae dentro de las tres cuñas. *Fuente*:
`results/part2/exact_regions_ibk1.csv` (`band_lower`, `band_upper`, `area`,
`coverage_a_in_b` del par ls, cw = 0.506 → 49.4 % fuera); §8.4–8.5.

**15. Donde el método se acaba: I-VU2** (0:50). *Se ve*: el problema 2 del
apéndice de [16]: `G_1 = [1, 1.5] x_1 + [1, 1.5] x_2 + [1, 1]`,
`G_2 = [1, 1.5] x_1² + [2, 3] x_2² − [1, 1]`, caja `[−4, 4]²`, con **x_1 y
x_2 a secas** resaltados (cambian de signo en la caja). Un dibujo pequeño: la
caja, el cuadrante `Q = [−4, 0]²` y la curva en L
`E = {(t, t/2): −4 ≤ t ≤ 0} ∪ {(−4, s): −4 ≤ s ≤ −2}`. Y una tabla de tres
filas "cierra / no cierra": φ_lu cierra (Opt = E); φ_ls no cierra (E ⊆ Opt ⊆
Q); φ_cw no cierra (E ⊆ Opt ⊆ Q). Frase: "los tres órdenes devuelven UN
conjunto, el del problema sin incertidumbre". *Se dice*: cuando un
coeficiente intervalar multiplica algo que cambia de signo, las dos funciones
frontera se intercambian — es la pregunta que los tutores plantearon el 4 de
septiembre —; en el origen el punto es óptimo bajo los tres órdenes
(demostrable en una línea) y a la vez la maquinaria publicada que genera
candidatos no se puede ni escribir allí; y el régimen se lee en los
coeficientes antes de correr nada: **ser intervalar de origen no basta**. No
se corrió a propósito. *Fuente*: §8.6. Esta diapositiva puede reducirse a una
frase dicha sobre la 14 si falta tiempo; los rayos singulares y la convexidad
se guardan para preguntas.

**16. Lo que salió de paso: el punto publicado como óptimo está dominado**
(1:00). *Se ve*: la tabla de cuatro filas. [16] publica
`x⋆ = (3.914930, 1.428474)` como Pareto óptimo de I-BK1 (Tabla 1, p. 20). Se
toma `y = (2.8975, 2.3975)`. Columnas: coordenada, G(y), G(x⋆) impreso,
margen: G_1 inf 1.414351 vs 1.736721; G_1 sup 3.403503 vs 3.677497; G_2 inf
1.119351 vs 1.393317; G_2 sup 4.712655 vs 6.731112. **Las cuatro
estrictamente menores** → x⋆ no es Pareto óptimo bajo la propia definición
2.17 de [16]. Debajo, una línea: "los tres solvers lo reproducen a ciegas: 18
de 18 configuraciones devuelven puntos que dominan a x⋆, sin que se les dijera
nada de él". *Se dice*: salió de aplicar el método, no de buscar errores; es
una corrección, no una crítica; los números de la derecha son los suyos y los
de la izquierda se recalculan con una calculadora en dos minutos; no es
redondeo (margen mínimo 0.274 frente a 4×10⁻⁶ de perturbación). Guarda para
preguntas: el conjunto crítico de su definición 2.18 es 4.24 veces el eficiente
(el mecanismo), y la frase literal de §9.5 sobre lo que **no** se afirma.
*Fuente*: §9.1–9.3; `results/part2/dominators_summary.csv`
(`seeds_with_a_dominator`, `widest_margin_over_seeds`);
`docs/part2/f2_ibk1_derivation.md` §4.2 para los cuatro valores.

### Cierre (1:30)

**17. Lo que se defiende, lo que se concede y lo que queda** (1:20). *Se ve*:
tres bloques cortos.
- *Se afirma*: la elección del orden no es un detalle de modelado — bajo una
  condición sobre el modelo de incertidumbre que se midió en vez de suponerse
  y que se comprueba antes de correr nada —; con magnitud exacta en un
  problema (10.3 % de unión compartida), medida en dos benchmarks con un
  instrumento cuyo sesgo se conoce (63–91 % fuera), y reproducida en un
  problema publicado por otros (tres conjuntos distintos, 49.4 %).
- *Se concede*: en I-BK1 los conjuntos se anidan y la magnitud de la parte 1
  no tiene equivalente; en I-VU2 los tres órdenes coinciden — ser intervalar
  de origen no basta; no se dice qué φ es mejor; ningún factor de corrección
  se transporta.
- *Queda*: I-IKK1 (un problema publicado con la estructura de p1, que
  decidiría si el anidamiento es de la anchura o de la procedencia); la curva
  de sensibilidad interpolando entre φ_lu y φ_cw (admisible por la propia
  definición de [1], el código lo permite, fue lo primero recortado); carteras
  como trabajo futuro (donde lo pone la diapositiva 21 de la propuesta).
*Se dice*: lo que queda y por qué cada cosa está donde está. Y las tres cosas
que no se saben (la mitad del déficit de NSGA-II, por qué p1 cruza e I-BK1
anida, por qué el error vale 1.81 en uno y 1.01–1.48 en otro) — que estén
escritas es parte del resultado. *Fuente*: `part2_closing.md` §8.3 y §12;
`explicacion_proyecto.md` §11 y Cierre.

**Diapositiva final** (0:10): "Gracias" + la pregunta de la 4 repetida en una
línea, o la imagen de la 7 en pequeño. Referencias [1], [7], [16] y
Mondal–Ghosh 2025 en una diapositiva de bibliografía aparte, fuera del
recorrido.

### Reserva (después de la bibliografía, sin numerar en el recorrido, con `\appendix`)

**R1. "¿Cómo sé que esto está bien?" — cinco trampas y cómo se detectaron.**
Cinco filas de tres columnas (qué pasa / cómo se detecta / qué estaba en
juego), una línea cada una: anchura constante (mide cero); anchura de ZDT1
alineada con el óptimo (comprobar donde vive el conjunto eficiente, no en la
caja); cancelación en coma flotante en la columna de la anchura (46 valores
salían como 210); aserción de puerta imposible por un minimizador protegido;
producto de intervalos que faltaba y anchura negativa silenciosa (arreglado sin
que se moviera ningún número, 40401 puntos bit a bit). *Fuente*: §10.

**R2. "¿Y los tres pares?" — la contención.** Criterio: una matriz no negativa
e invertible conserva la dominancia; aplicado a los coeficientes de los
Ejemplos 2.2, 2.3 y 2.4 sale X_lu ⊂ X_ls y X_cw ⊂ X_ls, y nada relaciona a
2.2 con 2.4 — por eso el par de cabecera es ése. Se usa sólo para retirar dos
pares, nunca para afirmar. Las coberturas que el criterio fija salen 1.000000
con recorrido 0 en todas las tiradas. Sigue abierta la pregunta de si está
publicado (Ishibuchi y Tanaka 1990, Prop. 4.2, es una comprobación para un
cuarto orden, no la respuesta). *Fuente*: §5.1.

**R3. "¿Y esto escala?" — el coste de pasar a 2m objetivos.** NSGA-II satura
el rango 1 en todas las semillas en las 24 configuraciones con imprecisión
positiva; generación en que ocurre (de 50): en DTLZ2, 2 bajo φ_ls y φ_cw; en
ZDT1, 23, 17, 15, 13 bajo φ_lu frente a 5 y 4–3 bajo los otros. Desde ahí el
frente es reparto, no convergencia; es la crítica de Cui et al. [7] a los
métodos de transformación con números propios. No dice que ningún solver esté
mal configurado. *Fuente*: §5.3, `results/tier1/rank_one_summary.csv`.

## 6. Reglas de diseño

- Una idea por diapositiva. Título = la frase que se quiere que recuerden, no
  un tema ("Toda la dependencia con ε es de un solo conjunto", no
  "Resultados tier 1").
- Máximo ~40 palabras de cuerpo por diapositiva salvo las tablas. Lo que no
  cabe va a `\note{}`.
- Fórmulas: sólo las que están en la sección 5. Nada de definición formal de
  automorfismo, gH-diferenciabilidad, Teorema 3.3 enunciado, ni condición (15).
  Los teoremas se nombran ("Teorema 3.3 y Ejemplo 3.9 de [1]"), no se
  enuncian.
- Figuras a página completa donde se indica (7, 14). Colores: los mismos tres
  colores para φ_lu, φ_ls, φ_cw en **toda** la presentación, definidos una vez;
  ninguno debe leerse como "bueno"/"malo" (no verde/rojo). Marca la
  intersección con rayado, no con un cuarto color.
- La 7 y la 16 son las dos diapositivas que hay que clavar. Si hay que
  recortar, se recorta la 12, luego la 15 (pasa a frase sobre la 14), luego la
  6; nunca la 7 ni la 16.
- Notas del orador con `\setbeameroption{show notes on second screen}` (o
  variante) activable con un flag; genera dos PDF: `presentacion.pdf`
  (limpio) y `presentacion_notas.pdf` (con notas).
- Numeración de página visible en el recorrido; no en las de reserva.

## 7. Entregables

Todo bajo `presentation/`:

- `presentation/presentacion.tex` — la presentación. Con `\input` de los
  fragmentos generados.
- `experiments/make_presentation.py` — el script que genera figuras y
  fragmentos desde `results/`. Debe correr con el `.venv` del repo (numpy y
  matplotlib están instalados) sin argumentos y ser idempotente.
- `results/figures/presentation/` — las figuras generadas y `fragments/`.
- `presentation/presentacion.pdf` y `presentation/presentacion_notas.pdf`,
  compilados con `lualatex` o `pdflatex` (dos pasadas). Adjunta el log si
  hay warnings de overfull box; corrígelos.
- `presentation/README.md` — media página: cómo regenerar, tabla de tiempos por
  diapositiva (debe sumar 15:00), lista de qué se recorta y en qué orden, y la
  lista de fichero → clave de la que sale cada número.

## 8. Comprobación final antes de entregar

Recorre la presentación compilada y confirma, una por una:

1. Ningún identificador de subparte, ni "pymoo", "semilla", "test", "delta",
   "tolerancia" aparece en el recorrido (grep sobre el `.tex`).
2. Ninguna frase ordena los φ ni usa "mejor/peor" sobre un φ.
3. El 1.81 aparece sólo en la diapositiva 10 y en la 17 como propiedad de p1.
4. Las dos concesiones están en la 14/15 y en la 17.
5. [1] se cita con tres autores en todas las apariciones.
6. Los ocho valores de la diapositiva 11 salen del CSV y caen en [62.8, 91.2] %.
7. Las áreas y fracciones de las 7 y 14 coinciden con `exact_regions_p1.csv`
   y `exact_regions_ibk1.csv`.
8. Las cuatro desigualdades de la 16 coinciden con
   `docs/part2/f2_ibk1_derivation.md` §4.2.
9. `make_presentation.py` corre desde cero y el `.tex` compila después sin
   tocar nada a mano.
10. Los tiempos del README suman 15 minutos.

Si algo del guion no lo puedes rastrear hasta un fichero de `results/` o de
`docs/`, **no lo inventes**: déjalo fuera de la diapositiva y anótalo en el
README como pendiente con la sección de `explicacion_proyecto.md` donde se
describe.
