# UNE 60670-5 · Sistemas de medición en estaciones de regulación con medida (ERM)

<p class="eyebrow">Tema 12 · Vídeo 2 de 2 · UNE 60670-5</p>

**Cuando la instalación es grande, medir el gas no es solo poner un contador: es todo un sistema de medición.** En este segundo vídeo entramos en las estaciones de regulación con medida (ERM): el contador y sus «acompañantes» —conversores de volumen, manómetros, termómetros y unidades de telemedida—, con sus clases, exactitudes y márgenes de trabajo. Terminamos con los anexos normativos A y B, que fijan los esquemas de medición según la potencia y el caudal. Aquí manda el detalle: porcentajes, clases de exactitud, diámetros de esfera y valores de memoria. Es material muy «de cifra», ideal para preguntas de examen.

## Sistemas de medición incorporados a estaciones de regulación con medida (ERM) en instalaciones receptoras

El sistema de medición incorporado a estas instalaciones debe disponer de las **unidades de medición necesarias** para cubrir los **caudales máximos y mínimos** del conjunto de instalaciones de utilización suministradas. Si existe una **etapa de regulación**, el sistema de medición debe ir **a continuación** de la misma.

Características mínimas de los sistemas de medición para las ERM, según la potencia de diseño:

- Potencia de diseño **inferior o igual a 70 kW**: las establecidas en el **anexo A**.
- Potencia de diseño **superior a 70 kW** suministradas con gases de la **segunda familia**: las establecidas en la **legislación vigente**.
- Potencia de diseño **superior a 70 kW** suministradas con gases de la **tercera familia**: las establecidas en el **anexo B**.

**Excepciones y sustituciones:**

- En los **conjuntos de regulación y medida** de los tipos **A-6, A-10-B y A-10-U** (según UNE 60404-1), el sistema de medición debe cumplir lo establecido en **dicha norma**, no siendo de aplicación los requisitos de este capítulo. Lo mismo ocurre con los conjuntos de regulación y medida según la Norma **UNE 60410**.
- Cuando el sistema de medición esté instalado **aguas abajo de un regulador** que cumpla la Norma **UNE 60402**, el manómetro y la válvula de contrastación exigidos pueden ser sustituidos por una **toma de presión tipo Peterson** a la salida del regulador.
- Cuando el sistema de medición esté **conectado directamente a una red de distribución con MOP inferior o igual a 0,025 bar**, el manómetro y la válvula de contrastación pueden ser sustituidos por una **toma de presión de débil calibre**.

**By-pass.** En las instalaciones de medida que dispongan de un **by-pass**, este debe permitir el **paso de la totalidad de gas directo** para la sustitución del contador o durante las operaciones de contrastación y/o mantenimiento. El by-pass debe ser **precintable, bloqueable y disponer de un disco ciego instalado**.

**Medida secundaria.** Las instalaciones de medición pueden ir provistas de un **sistema de medida secundario** que supla al de medida principal en caso de **avería o mantenimiento** del mismo.

> **Nota aclaratoria — la ERM, la «sala de máquinas» de la medición.** Piénsalo así: en una instalación pequeña basta un contador; en una grande hace falta un **conjunto** (contador + conversor + manómetro + termómetro + telemedida). El sistema de medición va **después del regulador** (primero se ajusta la presión, luego se cuenta). El tamaño de todo esto lo marca la **potencia**: hasta **70 kW** → anexo A; por encima → anexo B (tercera familia) o la legislación (segunda familia).

> **Nota aclaratoria — el by-pass, para no cortar el gas.** El **by-pass** es una tubería «de rodeo» para que el gas siga pasando mientras cambias o contrastas el contador (así no dejas al usuario sin servicio). Pero es peligroso dejarlo abierto sin control, por eso tres candados: **precintable** (sellado), **bloqueable** (no se abre por error) y con **disco ciego** puesto (tapón físico). Solo se usa en la maniobra puntual.

### Contadores

Los contadores pueden ser de **paredes deformables**, de **pistones rotativos (volumétricos)**, de **turbina (velocidad)** o de cualquier otro tipo que se halle **metrológicamente aceptado**.

**Dimensionamiento** (grado de gasificación según la Norma UNE 60670-4):

- En locales con **grado de gasificación 3**, los contadores deben estar dimensionados para trabajar en torno a los **márgenes de caudal entre el 60 % y el 85 %** del caudal máximo del contador.
- En locales de **grado de gasificación 1 y 2**, en torno a los **márgenes de caudal entre el 40 % y el 85 %**.

El dimensionamiento debe procurar que el contador trabaje, al menos la mayor parte de su tiempo de funcionamiento, **por encima del caudal de transición (Qt)**. Se entiende por caudal de transición aquel valor del caudal que se sitúa entre el caudal mínimo y el máximo y en el que el intervalo de caudal se divide en dos zonas, la **«zona superior»** y la **«zona inferior»**, correspondiendo a cada zona un **error máximo permitido característico** (según el RD 244/2016, que desarrolla la Ley 32/2014 de Metrología).

**Conformidad con normas:**

- **Paredes deformables**: Normas **UNE-EN 1359** y **UNE 60510**.
- **Turbina**: Norma **UNE-EN 12261**.
- **Pistones rotativos**: Norma **UNE-EN 12480**.
- **Domésticos ultrasónicos**: Norma **UNE-EN 14236** (metrológicamente aceptados).
- Otros contadores de ultrasonidos u otro tipo (masa, etc.) metrológicamente aceptados: conformes a **normas de reconocido prestigio internacional**.

La **elección** de uno u otro sistema de medición vendrá condicionada fundamentalmente por:

- El **tipo de régimen de consumo** del usuario/aplicación.
- El **campo válido de medida** según la dinámica elegida.

Todos los contadores que se instalen deben disponer de **emisores de impulsos proporcionales a los volúmenes brutos medidos**. En el caso de los contadores de **turbinas y pistones** es necesario que dispongan de un **doble emisor de impulsos**.

> **Nota aclaratoria — ni sobrado ni pillado.** El contador tiene que estar **bien dimensionado**: si es demasiado grande para el consumo, mide mal por abajo; si es pequeño, se ahoga. Por eso la norma da márgenes: **60-85 %** del caudal máximo en grado 3, y **40-85 %** en grados 1 y 2. Y siempre intentando que trabaje **por encima del Qt** (el caudal de transición), que es la frontera donde el contador es más preciso. Regla: *que el contador viva en su «zona buena», no en los extremos*.

> **Nota aclaratoria — el doble emisor de impulsos.** Cada contador manda «pulsos» proporcionales al gas que pasa (para telemedida). En los de **turbina y pistones** se exige **doble emisor**: dos señales, para poder detectar fraudes o fallos comparando ambas. En los de membrana (paredes deformables) basta con uno.

### Conversores de volumen

Para **gases menos densos que el aire**, la conversión del **volumen bruto** medido por un contador a **volumen en condiciones de referencia** se debe efectuar mediante **conversores de volumen** construidos de acuerdo con la Norma **UNE-EN 12405-1**.

Los conversores pueden ser:

- **Conversor Tipo PT**: con corrección por **presión y temperatura**.
- **Conversor Tipo PTZ**: con corrección por **presión, temperatura y factor de compresibilidad**, calculado a partir de las características físico-químicas del gas y de acuerdo con la Norma **UNE-EN ISO 12213**.

Los conversores deben ser de **clase C** con un **error máximo admisible de ± 0,5 %**, y deben incorporar una **pantalla de consulta** que permita, como mínimo, la visualización de:

- Volumen bruto.
- Volumen bruto en error.
- Volumen convertido.
- Volumen convertido en error.
- Presión y temperatura de medición.
- Factor de corrección global.
- Factor de compresibilidad, si este es calculado.

Deben disponer de **memoria** de los datos acumulados reglamentariamente requeridos de **como mínimo 35 días con discriminación horaria**, y disponer de una **salida serie** para conexión con equipos remotos.

Los **esquemas de instalación** son los establecidos en la legislación vigente y los recogidos en los **anexos A y B**.

> **Nota aclaratoria — el conversor «traduce» el volumen.** El gas ocupa más o menos según su presión y temperatura. El **conversor** pasa el volumen «bruto» (el que ve el contador) al volumen «de verdad» en condiciones de referencia, para facturar justo. Dos tipos: **PT** (corrige presión y temperatura) y **PTZ** (además el factor de compresibilidad Z, más fino). Cifras de examen: **clase C**, error **± 0,5 %** y memoria de **35 días** con detalle horario.

### Manómetros

La **elección** de los manómetros se debe hacer en función de las **presiones a indicar**, recomendándose que la **zona de trabajo** esté **entre el 35 % y el 75 % del fondo de escala**.

La instalación de todos los manómetros debe llevar incorporada una **válvula de tres vías de material metálico no oxidable** con **toma de ¼"** para conectar un **manómetro patrón de contrastación**.

En los casos en que se prevean **oscilaciones u otras perturbaciones** que puedan perjudicar la sensibilidad de los aparatos, se debe adoptar el adecuado **sistema de protección** (estrangulamiento, baños de aceite, etc.).

La **clase de exactitud** y el **diámetro de la esfera** deben ser, en función de la presión de la medida:

| Presión de la medida (P) | Esfera y clase de exactitud |
|---|---|
| P ≤ 0,08 bar | Esfera de Ø 80 mm o 100 mm y clase 1,6; o bien esfera de Ø 100 mm y clase 1 |
| 0,08 bar < P ≤ 0,4 bar | Esfera de Ø 100 mm y clase 1; o bien esfera de Ø 150-160 mm y clase 0,6 |
| P > 0,4 bar | Esfera de Ø 150-160 mm y clase 0,6 |

Los manómetros con **fondo de escala hasta 0,6 bar** son de **tipo cápsula** y deben cumplir la Norma **UNE-EN 837-3**, mientras que los de **fondo de escala igual o por encima de 0,6 bar** son de **tubo Bourdon** y han de cumplir la Norma **UNE-EN 837-1**. En ambos casos deben reflejar la **referencia de la norma** con la cual son conformes.

- Para los manómetros con **tope de aguja**, la clase de exactitud debe cubrir del **10 % al 100 %** de la escala.
- Para los manómetros con **cero libre**, la clase de exactitud debe cubrir del **0 % al 100 %** de la escala, y el **cero** debe servir de punto de control de la exactitud.

> **Nota aclaratoria — el manómetro trabaja «en el centro» de su escala.** Un manómetro se lee mejor si la aguja está entre el **35 % y el 75 %** del fondo de escala (ni pegada al cero ni al tope). Y siempre lleva una **válvula de tres vías con toma de ¼"** para enchufar un manómetro patrón y comprobar que no miente. Regla de la esfera: **a más presión, esfera más grande y clase más fina** (número de clase más bajo = más preciso: 1,6 → 1 → 0,6).

> **Nota aclaratoria — cápsula o Bourdon, la frontera está en 0,6 bar.** Dos familias de manómetro: **cápsula** (para presiones bajas, **hasta 0,6 bar**, norma **UNE-EN 837-3**) y **tubo Bourdon** (de **0,6 bar en adelante**, norma **UNE-EN 837-1**). El **0,6 bar** es la cifra bisagra que debes recordar, y el aparato debe llevar impresa la norma que cumple.

### Termómetros

La **escala de medición** para los termómetros debe ser, orientativamente, de **– 10 °C a + 60 °C**. Su **grado de exactitud** debe ser como mínimo de **± 0,5 °C**.

Deben disponer de una **protección tipo capilla** y se deben colocar dentro de **vainas resistentes de acero o latón** que permitan **extraer el termómetro sin interrumpir el servicio**.

Cuando el **diámetro de la tubería** no permita la colocación adecuada de la vaina del termómetro, se deben construir **botellas o ensanchamientos** que permitan la introducción de las vainas con la longitud necesaria para el bulbo, según instrucciones del suministrador del termómetro.

En todos los casos se deben **llenar y mantener las vainas con aceite mineral fluido** para mejorar las condiciones de transmisión de calor.

> **Nota aclaratoria — el termómetro va en una vaina con aceite.** El termómetro no toca el gas directamente: se mete en una **vaina** (funda) de acero o latón que se puede sacar **sin cortar el suministro**. Se rellena de **aceite mineral fluido** para que el calor pase bien del gas al bulbo. Números: escala de **–10 °C a +60 °C** y exactitud **± 0,5 °C**.

### Unidades remotas de telemedida

Los sistemas de medición que, de acuerdo con la reglamentación vigente, deban disponer de un **sistema de telemedida de consumos**, deben ir equipados con **unidades remotas de telemedida (UR)** de adquisición, almacenamiento y transmisión de datos, que se ajusten a las siguientes condiciones mínimas:

- Disponer como mínimo de una **entrada serie** para conexión con el conversor.
- Disponer de una **memoria mínima de almacenamiento** de los datos reglamentariamente requeridos **no inferior a 35 días**.
- Ser **compatibles con los sistemas de gestión de telemedida** del distribuidor y/o transportista, permitiendo la comunicación para la transmisión de datos.

> **Nota aclaratoria — telemedida: leer el contador desde la oficina.** La **unidad remota (UR)** recoge los datos del conversor y los envía a la compañía sin que nadie se acerque físicamente. Tres mínimos: una **entrada serie** (para hablar con el conversor), **35 días** de memoria (mismo número que el conversor) y ser **compatible** con el sistema del distribuidor/transportista. Si algo falla en la red, los 35 días guardan el histórico.

## Anexo A (Normativo) · Esquemas del sistema de medición en instalaciones de potencia de diseño ≤ 70 kW

**Figura A.1 – Segunda familia (gas natural).** Leyenda:

1. **Válvula de cierre.** Solo en el caso de que el contador sea de **caudal máximo superior a 10 m³/h** es necesario que también se incorpore una **llave a la salida** del mismo.
2. **Contador.**
3. **Toma de presión de débil calibre** (PC ≤ 150 mbar).

<figure>
<img src="imagenes_individuales/fig_7005_p017.png" alt="Esquema de medición Anexo A (≤ 70 kW): válvula, contador y toma de presión">
<figcaption>Figura A.1 (Anexo A, potencia ≤ 70 kW). Esquema básico de medición: válvula de cierre a la entrada (1), contador (2) y toma de presión (3). Cuando el contador es de más de 10 m³/h se añade también una válvula de cierre a la salida, como muestran las dos válvulas del esquema.</figcaption>
</figure>

**Figura A.2 – Tercera familia (GLP).** Leyenda:

1. **Válvula de cierre.**
2. **Contador.**
3. **Toma Peterson.**

> **Nota aclaratoria — esquema sencillo para lo pequeño (≤ 70 kW).** Hasta 70 kW el esquema es mínimo: **llave + contador + toma de presión**. La diferencia entre familias está en la toma: **débil calibre** (PC ≤ 150 mbar) para **gas natural**, y **toma Peterson** para **GLP**. Y ojo al detalle: si el contador es de **más de 10 m³/h**, hay que poner **también una llave a la salida**, no solo a la entrada.

## Anexo B (Normativo) · Esquemas del sistema de medición en instalaciones de potencia de diseño > 70 kW suministradas con gases de la tercera familia

**Tabla B.1 – Sistemas de medición en función del caudal máximo horario y el consumo final**

| Caudal máximo (*) [m³(n)/h] | Consumo anual ≤ 2 GWh | > 2 y ≤ 5 GWh | > 5 y ≤ 10 GWh | > 10 y ≤ 100 GWh | > 100 GWh |
|---|---|---|---|---|---|
| Q ≤ 150 | Fig. B.1 | Fig. B.1 | Fig. B.1 | Fig. B.2 | – |
| 150 < Q ≤ 350 | Fig. B.1 | Fig. B.1 | Fig. B.2 | Fig. B.2 | – |
| 350 < Q ≤ 600 | Fig. B.1 | Fig. B.1 | Fig. B.2 | Fig. B.2 | – |
| Q > 600 | – | Fig. B.2 | Fig. B.2 | Fig. B.2 | Fig. B.2 |

**NOTA 1** En las instalaciones de medición con esquema B.1 y B.2, la conversión se debe efectuar mediante **factor de conversión fijo** resultante de aplicar lo dispuesto en la legislación vigente.

**NOTA 2** En las instalaciones de medición a **presiones inferiores a 0,1 bar** **no** se deben instalar conversores de volumen.

(*) El caudal máximo (qmáx) se calcula a partir del **caudal máximo del contador**.

**Figura B.1.** Leyenda:

1. **Válvula de cierre.**
2. **Válvula de tres vías de acero inoxidable** con toma de ¼" para conectar manómetro patrón de contrastación.
3. **Manómetro** adecuado a la presión de trabajo, de acuerdo con lo indicado en el apartado de manómetros.
4. **Contador.**
5. **Toma de presión de débil calibre** (PC ≤ 150 mbar).

<figure>
<img src="imagenes_individuales/fig_7005_p018.jpeg" alt="Figura B.1: válvula, válvula de tres vías con manómetro, contador y toma de presión">
<figcaption>Figura B.1 (Anexo B, > 70 kW, tercera familia). En línea: válvula de cierre (1), válvula de tres vías (2) con el manómetro (3) para contrastación, contador (4) y toma de presión de débil calibre (5) a la salida.</figcaption>
</figure>

**Figura B.2.** Leyenda:

1. **Válvula de cierre.**
2. **Válvula de tres vías de acero inoxidable** con toma de ¼" para conectar manómetro patrón de contrastación.
3. **Manómetro** adecuado a la presión de trabajo, de acuerdo con lo indicado en el apartado de manómetros.
4. **Contador.**
5. **Disco en ocho.**

<figure>
<img src="imagenes_individuales/fig_7005_p019.png" alt="Figura B.2: esquema de medición con by-pass y disco en ocho">
<figcaption>Figura B.2 (Anexo B, > 70 kW, tercera familia). Como la B.1 pero con línea de by-pass inferior: válvula de cierre (1), válvula de tres vías (2) con manómetro (3), contador (4) y disco en ocho (5) sobre el by-pass para dejarlo ciego y precintado cuando no se usa.</figcaption>
</figure>

> **Nota aclaratoria — para lo grande (> 70 kW, GLP), la tabla manda.** Con potencias grandes de tercera familia, el esquema (B.1 o B.2) se elige cruzando dos datos en la **tabla B.1**: el **caudal máximo** (m³(n)/h) y el **consumo anual** (GWh). La diferencia entre B.1 y B.2 es el último elemento: **toma de presión de débil calibre** (B.1) frente a **disco en ocho** (B.2). Y dos avisos: la conversión es por **factor fijo**, y **por debajo de 0,1 bar no se ponen conversores**.

## Ideas clave del vídeo

- **Qué te llevas y para qué sirve.** Cuando la instalación crece (ERM), medir el gas ya no es «un contador y listo»: es un **conjunto** (contador + conversor + manómetro + termómetro + telemedida) que va **después del regulador** y se dimensiona por **potencia** (**≤ 70 kW** → anexo A; **> 70 kW** → anexo B en tercera familia o la legislación en segunda). Saber leer estos esquemas te sirve para montar el tren de medida en el orden correcto y para tener claro qué es tuyo y qué es del equipo de medida de la distribuidora.
- **El contador mal dimensionado se paga en facturación y en averías.** Trabaja al **60-85 %** del caudal máximo en grado de gasificación 3 y al **40-85 %** en grados 1 y 2, y siempre **por encima del Qt** (caudal de transición), su zona más precisa. Si lo pones **sobrado**, a caudales bajos **mide de menos** y llegan reclamaciones de facturación; si lo pones **corto**, se **ahoga**: pérdida de carga, presión que cae y **el aparato que no arranca a plena potencia o se apaga**. En **turbina y pistones**, **doble emisor de impulsos** para cruzar señales y cazar fallos o fraude.
- **El by-pass es cómodo y peligroso a partes iguales.** Deja pasar todo el gas mientras cambias o contrastas el contador (no dejas al usuario sin servicio), pero debe quedar **precintable, bloqueable y con disco ciego instalado**. Un by-pass **olvidado abierto** significa **gas sin medir** (fraude involuntario) y presión sin control aguas abajo. Solo se abre para la maniobra puntual y luego se vuelve a **precintar**.
- **Conversores: facturar el volumen «de verdad».** Pasan el volumen bruto al volumen en condiciones de referencia (**PT** corrige presión y temperatura; **PTZ** añade el factor de compresibilidad Z), según **UNE-EN 12405-1**. Datos de examen y de obra: **clase C**, error **± 0,5 %** y **memoria de 35 días** con discriminación horaria. Por debajo de **0,1 bar no se instalan conversores** (nota del anexo B). Un conversor mal parametrizado, o una vaina de termómetro **sin aceite**, falsean la temperatura y con ella **toda la facturación**.
- **Manómetros y termómetros: que no te mientan.** Manómetro trabajando entre el **35 % y el 75 %** del fondo de escala, con **válvula de tres vías metálica no oxidable** y toma de **¼"** para enchufar el patrón y **contrastar**. La frontera: **cápsula hasta 0,6 bar** (UNE-EN 837-3), **Bourdon de 0,6 bar en adelante** (UNE-EN 837-1); a más presión, **esfera mayor y clase más fina** (1,6 → 1 → 0,6). Termómetro de **–10 °C a +60 °C**, **± 0,5 °C**, en **vaina de acero o latón con aceite mineral**, extraíble **sin cortar el servicio**. Sin la válvula de tres vías no puedes verificar el manómetro sin parar la instalación.
- **Telemedida (UR).** **Entrada serie**, **≥ 35 días** de memoria y **compatibilidad** con el sistema del distribuidor/transportista. Si cae la red de comunicaciones, esos 35 días guardan el histórico para no perder consumos.
- **Esquemas y papeleo.** Anexo A (≤ 70 kW): **llave + contador + toma** (toma de **débil calibre** en gas natural, **Peterson** en GLP; y **llave también a la salida** si el contador pasa de **10 m³/h**). Anexo B (> 70 kW, tercera familia): eliges **B.1 o B.2** cruzando caudal y consumo en la **tabla B.1** (B.1 lleva toma de presión; B.2, **disco en ocho**). Recuerda que una **individual de más de 70 kW exige proyecto** y, con proyecto, **certificado de dirección de obra** de técnico competente además del **certificado de instalación**; el **equipo de medida es de la distribuidora**, que lo **precinta** en la puesta en servicio y lo somete al **control metrológico legal** (RD 244/2016). Sustituciones admitidas: **toma Peterson** aguas abajo de regulador **UNE 60402** y **toma de débil calibre** con red de **MOP ≤ 0,025 bar**.
