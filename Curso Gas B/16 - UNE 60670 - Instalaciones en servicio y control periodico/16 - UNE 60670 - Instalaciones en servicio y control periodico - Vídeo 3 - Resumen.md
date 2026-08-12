# UNE 60670-12 · Control periódico de instalaciones (individuales > 70 kW y comunes)

<p class="eyebrow">Tema 16 · Vídeo 3 de 4 · UNE 60670-12 · Control periódico de instalaciones (individuales > 70 kW y comunes)</p>

**Subimos de nivel: instalaciones grandes y de edificio.** Seguimos con la Parte 12, pero ahora en las instalaciones individuales de **potencia útil nominal superior a 70 kW** (con estación de regulación y medida) y en las **instalaciones receptoras comunes** (los montantes y recintos de contadores del edificio). Aquí aparece lo más «numérico» del tema: los **criterios de caudal de fuga en litros por hora** que deciden si una instalación es apta, apta pendiente de corrección o no apta. Domínalos.

## 1 · Instalaciones individuales de potencia útil nominal > 70 kW

Los códigos son **IPb** (principales) e **ISb** (secundarias).

### 1.1 Anomalías principales [IPb]

**IPb-1 · Fuga de gas.** Se debe realizar una **comprobación de estanquidad** de la instalación, **acometida interior, estación de regulación y medida (ERM) y líneas de distribución, hasta la llave de aparato**, mediante alguna de las técnicas del apartado 6.1 de la Norma **UNE 60670-11**. Si se detecta fuga, se actúa de una de estas formas:

**A) Gases menos densos que el aire**

- **a) Fuga localizada en un espacio interior del edificio considerado emplazamiento NO peligroso** (según la reglamentación vigente):
  - **a1) Midiendo el caudal de fuga** (con un método adecuado, a la presión de operación):
    - **Instalación no apta para uso:** caudal de fuga **superior a 5 l/h** → **anomalía principal IPb-1**. También se considera así **toda sala de máquinas** en la que el caudal de fuga sea **superior a 1 l/h** si dicha sala **no dispone de un sistema de detección y corte de gas** según la Norma **UNE 60601**.
    - **Instalación en aptitud de uso pendiente de corrección:** caudal de fuga **entre 1 l/h y 5 l/h** → **anomalía secundaria ISb-1**.
    - **Instalación en aptitud de uso:** caudal de fuga **inferior a 1 l/h** → **apta**.
  - **a2) No midiendo el caudal de fuga:** se considera **siempre no apta** para su uso y, por tanto, **anomalía principal IPb-1**.
- **b) Fuga localizada en un espacio interior considerado emplazamiento PELIGROSO, o fuga NO localizada:** en cualquiera de estas dos situaciones, **no apta** y **anomalía principal IPb-1**.
- **c) Fuga localizada en un tramo aéreo situado en el exterior del edificio:** si **no comporta riesgo potencial** → **anomalía secundaria ISb-1**; en el resto de los casos → **anomalía principal IPb-1**.
- **d) Tramo enterrado:** se aplica lo indicado en la Norma **UNE 60311**.

**B) Gases más densos que el aire**

En el caso de gases más densos que el aire se considera **siempre anomalía principal IPb-1, sin medir el caudal de fuga**.

> **Nota aclaratoria — la escalera de los litros/hora (¡memorízala!).** Para gas **menos denso que el aire** (gas natural), en interior no peligroso y **midiendo**:
>
> - **< 1 l/h** → **apta**.
> - **1 a 5 l/h** → **pendiente de corrección (secundaria ISb-1)**.
> - **> 5 l/h** → **no apta (principal IPb-1)**.
>
> Y las trampas: si **no mides**, siempre **no apta**. En **sala de máquinas** sin detección y corte de gas, el listón baja a **> 1 l/h** para ser no apta. Con gas **más denso que el aire** (GLP/propano, que se acumula en el suelo), **cualquier fuga es no apta, sin medir**. Truco: *el propano no perdona; pesa, se acumula y explota abajo*.

> **Nota aclaratoria — emplazamiento peligroso o fuga que no encuentras.** Si la fuga está en una zona clasificada como **peligrosa** (atmósfera potencialmente explosiva) o **no consigues localizarla**, no hay medición que valga: **no apta, principal**. No puedes dejar con gas algo cuyo fallo no sabes ni dónde está.

*(La reglamentación vigente que clasifica los emplazamientos peligrosos es el **Real Decreto 400/1996**, que transpone la Directiva ATEX sobre sistemas de protección para uso en atmósferas potencialmente explosivas.)*

### 1.2 Anomalías secundarias [ISb]

**ISb-1 · Fugas de gas secundarias.** Para considerar una fuga como secundaria (ISb-1) se atiende a lo indicado en el apartado de IPb-1 (caudal entre 1 y 5 l/h, o tramo aéreo exterior sin riesgo potencial).

**ISb-2 · Estado general de conservación defectuoso o materiales/técnicas de unión inadecuados.** Se considera anomalía secundaria:

- Materiales de **tuberías, soportes o uniones** en mal estado o con deficiencias (por ejemplo, **corrosión manifiesta**).
- **Llaves de corte** en malas condiciones, que falten o no sean accesibles (llave de usuario, llave de vivienda o llave de aparato).
- Estado **defectuoso del regulador de usuario** y/o de la **válvula de seguridad por mínima presión**.
- En instalaciones individuales **no conectadas a una instalación común**:
  - **Puerta o cerradura incorrecta** en armario de regulación y/o medida.
  - **Grietas apreciables visualmente** en las paredes interiores del armario de regulación y/o medida que posibiliten canalizar potenciales fugas de gas a la estructura del edificio.

**ISb-3 · Incumplimiento, apreciable a través de las partes visibles, de las condiciones del apartado 4.4 de la Norma UNE 60670-4** al discurrir tuberías por las **cavidades de altillos, falsos techos, cámaras y sótanos**.

**ISb-4 · Inexistencia o difícil accesibilidad de la llave general de usuario.** La llave general de usuario, o de inicio de instalación receptora, **debe existir** y **permitir su adecuada manipulación**. No deben existir **obstáculos** que impidan su accesibilidad, ni recurrir a **soluciones extrañas** (escaleras móviles, trampillas, etc.) para acceder a ella.

**ISb-5 · Estación de regulación con o sin medida sin toma de tierra y/o juntas dieléctricas.** Se considera esta anomalía cuando los dispositivos de la ERM **no estén conectados a tierra** mediante toma al efecto. Igualmente, si la ERM **no dispone de juntas aislantes** que la protejan de posibles corrientes eléctricas que puedan entrar en la estación, bien del tramo de **acometida interior** o de las **líneas de distribución**.

**ISb-6 · Ventilación del recinto de la ERM insuficiente o incorrecta.** Incumplimiento de los requisitos de ventilación descritos en el apartado 5.7 de la Norma **UNE 60620-3**.

**ISb-7 · Ubicación del recinto de la ERM y/o distancias mínimas de seguridad incorrectas.** Incumplimiento de los requisitos de ubicación de la ERM, en función de su clase y del tipo de recinto. Se debe comprobar la conformidad con los apartados 5.3, 5.4 y 5.5 (también en lo relativo a las **descargas de gas a la atmósfera**) de la Norma **UNE 60620-3**.

**ISb-8 · Inexistencia, deterioro o caducidad de la revisión del extintor de polvo seco.** En las inmediaciones del límite del recinto de la ERM y en el **exterior** del mismo, debe existir un **extintor de polvo seco, accesible, de capacidad igual a 12 kg**, y en **perfectas condiciones** de utilización.

**ISb-9 · La instalación eléctrica de la ERM incumple la normativa vigente.** Incumplimiento del apartado 7.3 de la Norma **UNE 60620-3**.

**ISb-10 · Inexistencia de la señalización correspondiente.** Incumplimiento del capítulo 6 de la Norma **UNE 60620-3**, en lo correspondiente a la señalización mediante **letreros**.

> **Nota aclaratoria — > 70 kW = aparece la ERM.** A partir de 70 kW la instalación es «industrial/terciaria» y suele tener **estación de regulación y medida (ERM)**. Por eso surgen anomalías que no verás en una vivienda: **toma de tierra y juntas dieléctricas** (ISb-5, para que no entren corrientes por la tubería), **ventilación y ubicación del recinto** (ISb-6, ISb-7), el **extintor de 12 kg** (ISb-8), la **instalación eléctrica** (ISb-9) y la **señalización** (ISb-10). Todas son **secundarias**.

> **Nota aclaratoria — el extintor de 12 kg.** Dato con truco: el extintor de polvo seco del recinto de la ERM es de **capacidad igual a 12 kg**, **accesible**, en el **exterior** del recinto y **revisado en fecha**. Si falta, está deteriorado o caducado → **ISb-8**. La cifra **12 kg** cae tal cual.

> **Nota aclaratoria — la llave general que no se alcanza.** ISb-4 es de sentido común: la llave general de usuario tiene que **estar** y poder **manejarse sin acrobacias**. Si para llegar a ella necesitas una escalera, abrir una trampilla o mover muebles, es anomalía. Una llave de corte que no puedes accionar en una emergencia no sirve de nada.

## 2 · Instalaciones receptoras comunes

Se consideran anomalías de las instalaciones comunes las que se indican a continuación. Los códigos son **CP** (principales) y **CS** (secundarias).

### 2.1 Anomalías principales [CP]

**CP-1 · Fuga de gas principal.** La comprobación de estanquidad de la instalación común se realiza mediante alguna de las técnicas del apartado 6.1 de la Norma **UNE 60670-11**. Si se detecta fuga:

**A) Gases menos densos que el aire**

- **a) Fuga localizada en un espacio interior del edificio considerado emplazamiento NO peligroso:**
  - **a1) Midiendo el caudal de fuga** (a la presión de operación):
    - **No apta para uso:** caudal **superior a 5 l/h** → **anomalía principal CP-1**.
    - **Aptitud de uso pendiente de corrección:** caudal **entre 1 l/h y 5 l/h** → **anomalía secundaria CS-1**.
    - **Aptitud de uso:** caudal **inferior a 1 l/h** → **apta**.
  - **a2) No midiendo el caudal de fuga:** se considera **siempre no apta** y, por tanto, **anomalía principal CP-1**.
- **b) Fuga localizada en emplazamiento PELIGROSO, o fuga NO localizada:** en ambos casos, **no apta** y **anomalía principal CP-1**.
- **c) Fuga localizada en un tramo aéreo exterior del edificio:** si **no comporta riesgo potencial** → **anomalía secundaria CS-1**; en el resto de los casos → **anomalía principal CP-1**.
- **d) Tramo enterrado:** se aplica lo indicado en la Norma **UNE 60311**.

**B) Gases más densos que el aire**

Se considera **siempre anomalía principal CP-1, sin medir el caudal de fuga**.

> **Nota aclaratoria — misma escalera de litros, otras siglas.** La fuga en instalación **común** usa exactamente los mismos números que la individual > 70 kW: **< 1 l/h apta**, **1-5 l/h pendiente (secundaria CS-1)**, **> 5 l/h no apta (principal CP-1)**; sin medir = no apta; gas más denso = no apta sin medir. Solo cambian las siglas: **CP/CS** en común, **IPb/ISb** en individual grande. La única diferencia de fondo: en común **no** aparece el matiz especial de la sala de máquinas (> 1 l/h).

### 2.2 Anomalías secundarias [CS]

**CS-1 · Fugas de gas secundarias.** Para considerar una fuga como secundaria (CS-1) se atiende a lo indicado en CP-1 (caudal entre 1 y 5 l/h, o tramo aéreo exterior sin riesgo potencial).

**CS-2 · Conjunto de regulación situado en un local interior del edificio y ubicado en un armario que no ventile directamente al exterior.** Se considera anomalía la **inexistencia de ventilación directa al exterior** del armario de regulación cuando dicho armario esté en un local interior del edificio.

**CS-3 · Ventilación del recinto de centralización de contadores insuficiente o incorrecta.** Incumplimiento de los requisitos de ventilación del recinto de centralización de contadores descritos en la **tabla 1 del apartado 5.4 de la Norma UNE 60670-5**.

**CS-4 · Estado general de conservación defectuoso o materiales/técnicas de unión inadecuados.** Se considera anomalía secundaria:

- Materiales de **tuberías, soportes, protecciones o uniones** en mal estado o con deficiencias (por ejemplo, **corrosión manifiesta**).
- **Llaves de corte** en malas condiciones, que falten o no sean accesibles (**llave general**).

**CS-5 · Incumplimiento, apreciable a través de las partes visibles, de las condiciones del apartado 4.4 de la Norma UNE 60670-4** al discurrir tuberías por las **cavidades de altillos, falsos techos, cámaras y sótanos**.

**CS-6 · Evidente mal estado de conservación de la instalación eléctrica en el recinto de contadores.**

**CS-7 · Existencia de instalaciones ajenas al mismo en el recinto de contadores**, o **incorrecta ejecución** de las mismas.

**CS-8 · Puerta o cerradura incorrecta en armario de regulación o en recinto de contadores.** Se considera también anomalía la **no existencia de puerta**.

**CS-9 · Existencia de grietas, apreciables visualmente, en las paredes interiores del recinto de contadores, reguladores o colectores de llaves**, que posibiliten canalizar potenciales fugas de gas a la estructura del edificio. En el caso de **gas natural** estas grietas se evalúan en la **zona del techo del recinto y la que queda por encima de la rejilla de ventilación superior**. En el caso de **GLP** se comprueba el **suelo del recinto y la zona que queda por debajo de la rejilla de ventilación inferior**.

**CS-10 · Falta de identificación de los contadores** (en centralización de contadores) **o de las llaves de usuario** (en centralizaciones de llaves).

> **Nota aclaratoria — dónde miras las grietas: arriba o abajo según el gas.** CS-9 tiene un detalle finísimo y muy preguntable. El gas natural es **más ligero que el aire**: sube, así que las grietas peligrosas están **arriba** (techo y por encima de la rejilla superior). El GLP es **más pesado**: baja, así que buscas grietas **abajo** (suelo y por debajo de la rejilla inferior). Regla: *natural, mira al techo; GLP, mira al suelo*. La misma lógica del «GN sube, GLP baja» explica muchísimas cosas.

> **Nota aclaratoria — el recinto de contadores es solo para el gas.** Varias anomalías comunes (CS-6, CS-7, CS-8) vigilan que el recinto de contadores esté limpio de intrusos: nada de **instalaciones eléctricas en mal estado**, nada de **instalaciones ajenas** (cuartos que se usan de trastero, cables de otras cosas), y con su **puerta** en condiciones (o directamente, que la puerta **exista**). Un recinto de gas no es un almacén.

> **Nota aclaratoria — identificar contadores y llaves (CS-10).** En un edificio con muchos contadores o muchas llaves de usuario, cada uno tiene que estar **etiquetado** con su vivienda. Si no sabes qué contador es de qué piso, en una emergencia cortas a ciegas. Por eso la falta de identificación es anomalía (secundaria).

## Ideas clave del vídeo

- Instalaciones **individuales > 70 kW**: principales **IPb-1** (fuga), secundarias **ISb-1 a ISb-10**. Aparece la **ERM** y sus anomalías propias (toma de tierra/juntas, ventilación, ubicación, **extintor de 12 kg**, instalación eléctrica, señalización).
- **Criterio de fuga (gas menos denso, interior no peligroso, midiendo):** **< 1 l/h** apta · **1-5 l/h** pendiente (secundaria) · **> 5 l/h** no apta (principal). **Sin medir → no apta.** **Sala de máquinas** sin detección y corte: no apta ya con **> 1 l/h**.
- **Gas más denso que el aire (GLP): cualquier fuga es no apta, sin medir.** Emplazamiento peligroso o fuga no localizada → **no apta**. Tramo aéreo exterior sin riesgo → secundaria. Tramo enterrado → **UNE 60311**.
- Instalaciones **comunes**: principales **CP-1** (misma escalera de litros/hora, siglas CP/CS), secundarias **CS-1 a CS-10**.
- **CS-9 (grietas):** en **gas natural**, mirar **arriba** (techo y sobre la rejilla superior); en **GLP**, mirar **abajo** (suelo y bajo la rejilla inferior).
- El **recinto de contadores** debe estar libre de instalaciones ajenas, con instalación eléctrica en buen estado, con **puerta** correcta y con contadores/llaves **identificados**.
