# LMMarkovChain

### En qué consiste?

El uso de las cadenas de Markov en la generación de lenguaje se basan en los *n-grams*, puesto que, una vez conozemos que palabras suelen estar cerca de otras en un texto, podemos crear un modelo estadístico, y predecir de esta forma, qué palabras pueden aparecer a continuación.

Pueden existir de distintos órdenes según el número anterior de palabras que se tienen en cuenta para la predicción.

- Primer Orden: Token -> Predicción 

- Segundo Orden: Token -> Token -> Predicción

- Orden N: Nº Tokens -> Predicción


### Ventajas e Inconvenientes

#### Ventajas:

- Implementación simple ya que son fáciles de entender a la hora de generar texto.

- Requieren menos recursos computacionales en comparación a otros modelos más complejos.

- La velocidad de generación de texto es rápida.

- No requiere datos etiquetados para entrenar al modelo ya que se basa en la frecuencia  de aparición de la secuencia de palabras 

#### Inconvenientes:

- Falta de coherencia en el texto generado ya que el modelo no tiene comprensión del contenido.

- Es común que el texto sea repetitivo y carezca de variedad, ya que se fija en los datos con los que se ha entrenado.

- Para obtener un buen resultado hace falta un texto de tamaño considerable.

- Puede generar texto que no siga las reglas gramaticales correctas.

### Aplicaciones (viables)

- Sistemas de corrección de textos.

- Sugerencias en editores de textos (ejemplo práctico en teléfonos móviles).

- Análisis y simulación de secuencias de caracteres en criptografía.

# Ejemplos

#### Comando usado :

```console
# Texto juego de tronos orden 7
python generator_adv.py sample_text/jt.txt 7
```

#### Salida:

- *Trató de arrastrarse hacia la tienda, pero Cohollo la agarró por el pelo y le puso un cuchillo contra la garganta.*

#### Comando usado :

```console
# Texto juego de tronos orden 4 palabra inicio 'patio'
python generator_adv.py sample_text/jt.txt 4 patio
```

#### Salida:

- *patio en dirección a sus habitaciones, situadas en la Torre del Lord Comandante, levantando la nieve a su paso.*

#### Comando usado :

```console
# Texto juego de tronos orden 2 palabra inicio 'brazo' 5 oraciones
python generator_5.py sample_text/jt.txt brazo
```

#### Salida:

- *brazo derecho, desde el risco más lejano, al otro lado de las ropas más abrigadas.*

- *brazo extendido, más allá de esta historia igual que no diera crédito a las doncellas.*

- *brazo con tanta fuerza que tienes? —se mofó Mormont—. ¿Tan cerca del agua, pero sí con el ceño fruncido.*

- *brazo muerto se salía con la parte superior de las lágrimas.*

- *brazo un y elmo blanco, el murciélago que era él.*

# Instalación

```console
conda create -n markovify python=3.10
conda activate markovify
python install markovify
```

# Uso

```console
conda activate markovify
python *script a usar*
```
